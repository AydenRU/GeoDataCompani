from typing import Annotated

from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.session import get_session
from app.repositories.check_activate import CheckDb

async def check_connect_with_db(request: AsyncSession) -> HTTPException:
    """Получение информации о состоянии подключения
    Args:
        request: Сессия подключения
    Return:
        HTTPException 200, если есть подключение или 400
    """
    try:
        repositories = CheckDb(request)
        answer = await repositories.check_connection_db()

        return HTTPException(status_code=200, detail='База подключена', headers= answer)
    except Exception as error:
        return HTTPException(status_code=500, detail='Подключение отсутствует')