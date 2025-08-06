from typing import Annotated

from fastapi import APIRouter, status, Depends
from fastapi import  Request
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.check import check_connect_with_db

from app.core.session import get_session

router_check = APIRouter(prefix='/health', tags=['Check'])


@router_check.get('/check_status_db',
                        status_code=status.HTTP_200_OK,
                        summary='Получить статус базы данных')
async def endpoint_check_db(request: Annotated[AsyncSession, Depends(get_session)]):
    """Проверка на подключение к БД
    return:
        Вернет HTTPException 200 если БД подключена в противном случае вернет 500"""
    return await check_connect_with_db(request)


@router_check.get('/liveness',
                  status_code=status.HTTP_200_OK,
                  summary='Получить статус приложения')
async def check_app_endpoint():
    """Получение информации о запросе
    raise:
        HTTPException 200 если приложение активно
    """
    raise HTTPException(status_code=200, detail='Приложение активно')
