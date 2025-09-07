from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.authorization_services import AuthorizationServices

from app.core.authorisation import auth
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
        session = AuthorizationServices(session)
        answer = await session.get_data_user(data_user, response)
    except Exception as error:
        raise error

    return {'access_token': answer[0],
            'refresh_token': answer[1],
            'text': 'Ты вошел'}


