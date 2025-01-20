from fastapi import APIRouter, status, Header
from fastapi.responses import JSONResponse

from src.schemas.users import CreateUserSchema
from src.database.crud import insert_user
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
