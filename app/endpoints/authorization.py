from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import Request, Response

from app.core.authorisation import auth

from app.schemas.login import AuthorisationUser

router_authorization = APIRouter(prefix='/login', tags=['authorization'])


@router_authorization.post('/login')
async def check_users(data_user: AuthorisationUser) -> dict:
    """
    Аутентификация пользователя
    arg:
        data_user: pydentic shema
            username: имя пользователя
            password: пароль пользователя
    return: какие-то данные
    """
    if data_user.username == 'ayden' and data_user.password == 'ayden':
        token = auth.create_access_token(uid=data_user.username, data={'username': data_user.username})
        Response.set_cookie(auth.config.JWT_ACCESS_COOKIE_NAME, token)
        return {'token': token,
                'text': 'Ты вошел'}

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)