from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager

from app.repositories.database import create_network_with_db, text

from app.endpoints.check_work_app import  check_work_app_router

from app.models.models import metadata_db

@asynccontextmanager
async def lifespans(app: FastAPI):
    print("Начало подключения..")
    app.state.connect_db = await create_network_with_db()
    async with app.state.connect_db.begin() as conn:
        await conn.run_sync(metadata_db.drop_all)
        await conn.run_sync(metadata_db.create_all)
    print('база подключена')
    yield
    print("Конец подключения...")


app = FastAPI(lifespan=lifespans)
app.include_router(check_work_app_router)

if __name__ == '__main__':
    uvicorn.run('app.main:app')