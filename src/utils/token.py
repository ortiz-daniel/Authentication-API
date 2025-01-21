from jwt import decode, encode, ExpiredSignatureError
from dotenv import load_dotenv
import os
import datetime
from datetime import timezone

load_dotenv(f'{os.getcwd()}/.env.dev')

class Token:

    @staticmethod
    def encode_token(body: dict) -> str:
        print(os.getenv('TOKEN_EXP_IN_MINUTES'))
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
    def decode_token(token: str):

        try:
            decoded_token = decode(
                token,
                key=os.getenv('SECRET_KEY'),
                algorithms=[os.getenv('ALGORITHM')]
                )
        except ExpiredSignatureError as e:
            # Manejo correcto de este error
            return {'error': 'Token inválido'}
        
        return decoded_token

