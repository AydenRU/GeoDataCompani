from fastapi import APIRouter, Request

from fastapi import HTTPException

from app.services.check import check_connect_with_db


check_work_app_router = APIRouter(prefix='/health', tags=['Check'])



@check_work_app_router.get('/check_status_db')
async def endpoint_check_db(request: Request):
    """Проверка на подключение к БДа"""
    return await check_connect_with_db(request)


@check_work_app_router.get('/liveness')
async def check_app_endpoint():
        raise HTTPException(status_code=200, detail='Приложение активно')


