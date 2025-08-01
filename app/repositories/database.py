from sqlalchemy.ext.asyncio import  create_async_engine, async_sessionmaker
from sqlalchemy import text

from app.core.conf import SettingDB

# # для типизации
from  sqlalchemy.ext.asyncio import AsyncSession


setting = SettingDB()

db = create_async_engine(
        url=setting.async_address_URL_DB(),
        pool_size=5,
        max_overflow=10
)
async_session = async_sessionmaker(db)

async def postgis(session_db):
        async with session_db() as conn:
            await conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis;"))
            await conn.commit()

