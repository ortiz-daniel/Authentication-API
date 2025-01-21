from jwt import decode, encode, ExpiredSignatureError, DecodeError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request
from dotenv import load_dotenv
import os
import datetime
from datetime import timezone

load_dotenv(f'{os.getcwd()}/.env.dev')

class Token:

    @staticmethod
    def encode_token(body: dict) -> str:
        payload: dict = {
            **body,
            "exp": datetime.datetime.now(timezone.utc) + datetime.timedelta(
                minutes=int(os.getenv('TOKEN_EXP_IN_MINUTES'))
                )
            }
        token: str = encode(
            payload,
            key=os.getenv('SECRET_KEY'),
            algorithm=os.getenv('ALGORITHM')
            )
        return token

    @staticmethod
    def decode_token(token: str) -> dict:

        try:
            decoded_token = decode(
                token,
                key=os.getenv('SECRET_KEY'),
                algorithms=[os.getenv('ALGORITHM')]
                )
        except ExpiredSignatureError as e:
            return {
                'error': 'Le fecha de expiración del token ha sido superada. Intenta iniciar sesión nuevamente.'
                }
        except DecodeError as e:
            return {
                'error': 'El token es inválido. Intenta iniciar sesión nuevamente.'
                }
        return decoded_token

class TokenDependencie(HTTPBearer):
    def __init__(self):
        super(TokenDependencie, self).__init__()
    
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(TokenDependencie, self).__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=403, detail='El esquema del token es inválido.')
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail='El token es inválido.')
