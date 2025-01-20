from fastapi import APIRouter, status, Header, Depends
from fastapi.security import HTTPBearer
from fastapi.responses import JSONResponse
from typing import Annotated

from src.schemas.users import CreateUserSchema
from src.database.crud import insert_user, get_user_by_email
from src.database.models import User
from src.utils.token import Token

router: APIRouter = APIRouter(prefix='/users', tags=["Users"])  

@router.post('/', response_model=CreateUserSchema)
async def create_user(body: CreateUserSchema):
    """
    Servicio que permite la creación de nuevos usuarios en la aplicación.

    El servicio recibe un JSON con los datos del usuario a crear y retorna un mensaje de éxito
    al mismo tiempo que el token de autenticación con una expiración de 2 minutos.

    Returns:
        JSON: Mensaje de éxito, usuario y token de autenticación.
    """

    body_to_dict: dict = body.dict()

    user_inserted: User = insert_user(body_to_dict)

    token: str = Token.encode_token(body_to_dict)

    response: dict = {
        'message': 'Usuario creado con éxito',
        'user': user_inserted.dict(exclude={'password'}),
        'token': token
        }
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=response)


@router.post('/login')
def login(body: CreateUserSchema):
    """
    Función que permite la autenticación de usuarios en la aplicación.

    Returns:
        JSON: Mensaje de éxito y token de autenticación con expiracion de 2 minutos a partir de la fecha de creación.
    """
    
    body_to_dict: dict = body.dict()

    user: User = get_user_by_email(body_to_dict['email'])

    if user is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'message': 'Usuario no encontrado'}
            )
    else:
        if user.password == body_to_dict['password']:
            token: str = Token.encode_token(body_to_dict)
            response: dict = {
                'message': 'Usuario autenticado con éxito',
                'token': token
                }
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=response
                )
        else:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={'message': 'Contraseña incorrecta'}
                )
