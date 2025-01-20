from jwt import decode, encode
from dotenv import load_dotenv
import os
import datetime

load_dotenv(f'{os.getcwd()}/.env.dev')

class Token:

    @staticmethod
    def encode_token(body: dict) -> str:
        print(os.getenv('TOKEN_EXP_IN_MINUTES'))
        payload: dict = {
            **body,
            "exp": datetime.datetime.now() + datetime.timedelta(
                minutes=int(os.getenv('TOKEN_EXP_IN_MINUTES'))
                )
            }
        token: str = encode(
            payload,
            os.getenv('SECRET_KEY'),
            algorithm=os.getenv('ALGORITHM')
            )
        return token
