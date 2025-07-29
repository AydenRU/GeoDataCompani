
from fastapi import Request, HTTPException

from app.repositories.check_activate import check_connection_db

async def check_connect_with_db(request: Request):
    try:
        answer = await check_connection_db(request.app.state.session_db)

        return HTTPException(status_code=200, detail='База подключена', headers= answer)
    except Exception as error:

        return HTTPException(status_code=400, detail='Подключение отсутствует')