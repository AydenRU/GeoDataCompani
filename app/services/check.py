

from fastapi import Request ,HTTPException

from app.repositories.check_activate import test

async def check_connect_with_db(request: Request):
    try:
        answer = await test(request.app.state.session_db)

        return HTTPException(status_code=200, detail='База подключена', headers= answer)
    except Exception as error:

        return HTTPException(status_code=400, detail='Подключение отсутствует')