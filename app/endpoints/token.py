from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.authorization_services import AuthorizationServices

from app.core.authorisation import auth, CheckToken
from app.core.hash import my_hash
from app.core.session import get_session

from app.schemas.login import AuthorisationUser

router_authorization = APIRouter(prefix='/login', tags=['authorization'])


@router_authorization.post('/login',
                           summary='Вход пользователя в аккаунт',
                           status_code=status.HTTP_200_OK)
async def login(data_user: AuthorisationUser, response: Response, session: AsyncSession = Depends(get_session)) -> dict:
    """
    Аутентификация пользователя
    arg:
        data_user: pydentic shema
            username: имя пользователя
            password: пароль пользователя
    return: какие-то данные
    """
    try:
        service = AuthorizationServices(session)
        answer = await service.get_data_user(data_user, response)
    except Exception as error:
        raise error

    return {'access_token': answer[0],
            'refresh_token': answer[1],
            'text': 'Ты вошел'}

@router_authorization.post('/refresh',
                           summary='Обрабатывает refresh токен и возвращает новый access токен',
                           status_code=status.HTTP_200_OK)
async def refresh_jwt_token_in_access(data_token: Annotated[dict, Depends(CheckToken.check_refresh_token)],
                                      session: Annotated[AsyncSession, Depends(get_session)],
                                      response: Response) :
    """Проверка Refresh token и генерация нового Access token"""
    service = AuthorizationServices(session)
    try:
        answer = await service.generation_new_access_token(data_token, response)

        return {'access_token': answer}
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


