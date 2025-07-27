from fastapi import APIRouter, Request

from fastapi import HTTPException

from app.repositories.database import test


check_work_app_router = APIRouter(prefix='/health', tags=['Check'])



@check_work_app_router.get('/check_status_db')
async def check_db(request: Request):
    """Проверка на подключение к БД"""
    try:
        answer = await test(request.app.state.connect_db)

        return HTTPException(status_code=200, detail='База подключена')
    except Exception as error:

        return HTTPException(status_code=400, detail='Подключение отсутствует')