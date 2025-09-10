from fastapi import FastAPI

from contextlib import asynccontextmanager


from app.repositories.database import db, async_session
from app.core.conf import setting_redis

from app.endpoints.check_work_app import router_check
from app.endpoints.organizations import router_organizations
from app.endpoints.token import router_authorization
from app.endpoints.registration import router_registration

from app.repositories.check_activate import CheckDb
from app.db.loading_data import to_go_load_test_data


@asynccontextmanager
async def lifespans(app: FastAPI):
    """функция запускаемая в начале работы FastAPI"""
    app.state.engine = db
    app.state.session_db = async_session
    app.state.redis = setting_redis.async_connection_redis()


    async with app.state.session_db() as session:
        if not await CheckDb.check_empy_data_db(session):
            await to_go_load_test_data(session)
    yield


app = FastAPI(lifespan=lifespans)
app.include_router(router_check)
app.include_router(router_organizations)
app.include_router(router_authorization)
app.include_router(router_registration)