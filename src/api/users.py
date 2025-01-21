from fastapi import APIRouter, status, Header, Depends
from fastapi.responses import JSONResponse

from src.schemas.users import CreateUserSchema
from src.database.crud import insert_user, get_logins_by_user
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

@router.get('/sessions')
def get_sessions_history(token: str = Header(...)):
    """
    Servicio que permite obtener el historial de sesiones de un usuario autenticado.

    El servicio requiere de un token de autenticación para poder obtener el historial de sesiones.

    El servicio recibe el email del usuario y retorna un JSON con el historial de sesiones.

    Returns:
        JSON: Historial de sesiones del usuario.
    """

    body: dict = Token.decode_token(token)

    if 'error' in body:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=body
            )

    logins = get_logins_by_user(body['email'])

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'message': 'Historial de sesiones',
            'history_sessions': logins
        }
    )
