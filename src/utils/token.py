from jwt import decode, encode, ExpiredSignatureError, DecodeError
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

