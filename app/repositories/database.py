from sqlalchemy.ext.asyncio import  create_async_engine, async_sessionmaker
from sqlalchemy import text

from app.core.conf import setting_db

# # для типизации
from  sqlalchemy.ext.asyncio import AsyncSession



db = create_async_engine(
        url=setting_db.async_address_URL_DB(),
        pool_size=5,
        max_overflow=10
)
async_session = async_sessionmaker(db)

async def postgis(session_db: AsyncSession):
        async with session_db() as conn:
            await conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis;"))
            await conn.commit()



# async def create_network_with_db():
#     return create_async_engine(
#         url=setting_db.async_address_URL_DB(),
#         pool_size=5,
#         max_overflow=10,
#     )
#
# async def test(create_db: AsyncEngine):
#     async with create_db.connect() as conn:
#         answer = await conn.execute(text('SELECT version()'))
#         # print(answer.first())
#         return {'version': str(answer.first())}
