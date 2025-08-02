from fastapi import APIRouter, Request

from fastapi import HTTPException

from app.services.check import check_connect_with_db

router_check = APIRouter(prefix='/health', tags=['Check'])


@router_check.get('/check_status_db')
async def endpoint_check_db(request: Request):
    """Проверка на подключение к БДа"""
    return await check_connect_with_db(request)


@router_check.get('/liveness')
async def check_app_endpoint():
    raise HTTPException(status_code=200, detail='Приложение активно')
