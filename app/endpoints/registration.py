from asyncio import start_unix_server

from fastapi import APIRouter, HTTPException, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.registration_services import RegistrationServices

from app.core.session import get_session
from app.schemas.registration import RegistrationUser


router_registration = APIRouter(prefix='/registr', tags=['registration'])


@router_registration.post('/',
                          summary='Получение данных для регистрации уникального пользователя',
                          status_code=status.HTTP_200_OK)
async def registration(data_user: RegistrationUser, session: AsyncSession = Depends(get_session)) -> dict:
    """Производим регистрацию пользователя
    args:
        data_user: RegistrationUser,
        session: AsyncSessio

    return:
        status_code=status.HTTP_200_OK

    raise:
        В случае ошибку вернется исключение HTTPException 400
    """
    services = RegistrationServices(session)
    try:
        await services.registration(data_user)
        return {'status_code': 'OK'}
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)