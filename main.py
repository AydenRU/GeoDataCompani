from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager

from app.repositories.database import db, async_session

from app.endpoints.check_work_app import  check_work_app_router
from app.endpoints.organizations import  router_organizations

from app.db.loading_data import to_go_load_test_data

from app.models.models import Base
from app.repositories.database import postgis

# from app.models.models import metadata_db

@asynccontextmanager
async def lifespans(app: FastAPI):
    print("Начало подключения..")
    app.state.engine = db
    app.state.session_db = async_session

    await postgis(app.state.session_db)

    async with app.state.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await to_go_load_test_data(app.state.session_db)
    print('база подключена и данные загружены')
    yield
    print("Конец подключения...")

    # app.state.connect_db = await create_network_with_db()
    # async with app.state.connect_db.begin() as conn:
    #     await conn.run_sync(metadata_db.drop_all)
    #     await conn.run_sync(metadata_db.create_all)
    #

    # print('база подключена')
    # yield
    # print("Конец подключения...")


app = FastAPI(lifespan=lifespans)
app.include_router(check_work_app_router)
app.include_router(router_organizations)

if __name__ == '__main__':
    uvicorn.run('main:app')