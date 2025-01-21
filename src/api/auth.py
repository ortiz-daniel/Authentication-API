from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.schemas.users import CreateUserSchema
from src.database.crud import get_user_by_email, insert_login_session
from src.utils.token import Token

router: APIRouter = APIRouter(prefix='/auth', tags=["Users"])  

@router.post('/login')
def login(body: CreateUserSchema):
    """
    Servicio que permite la autenticación de usuarios en la API.

    El servicio recibe un JSON con los datos del usuario a autenticar y retorna un mensaje de éxito.

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
            
            insert_login_session(user.email, True)

            response: dict = {
                'message': 'Usuario autenticado con éxito',
                'token': token
                }
            
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=response
                )
        else:
            
            insert_login_session(user.email, False)
            
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={'message': 'Contraseña incorrecta'}
                )
