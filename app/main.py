from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager

from app.repositories.database import db, async_session


from app.endpoints.check_work_app import router_check
from app.endpoints.organizations import router_organizations

from app.repositories.check_activate import CheckDb
from app.db.loading_data import to_go_load_test_data


@asynccontextmanager
async def lifespans(app: FastAPI):
    print("Начало подключения..")
    app.state.engine = db
    app.state.session_db = async_session

    async with app.state.session_db() as session:
        if not await CheckDb.check_empy_data_db(session):
            await to_go_load_test_data(session)
    print('база подключена и данные загружены')
    yield
    print("Конец подключения...")


app = FastAPI(lifespan=lifespans)
app.include_router(router_check)
app.include_router(router_organizations)

# if __name__ == '__main__':
#     uvicorn.run('app.main:app')
