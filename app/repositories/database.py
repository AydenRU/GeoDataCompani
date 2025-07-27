from fastapi import FastAPI
from sqlalchemy.ext.asyncio import  create_async_engine, AsyncSession
from sqlalchemy import text



from app.core.conf import setting_db

# для типизации
from  sqlalchemy.ext.asyncio.engine import AsyncEngine


import asyncio

async def create_network_with_db():
    return create_async_engine(
        url=setting_db.async_address_URL_DB(),
        pool_size=5,
        max_overflow=10,
    )

async def test(create_db: AsyncEngine):
    async with create_db.connect() as conn:
        answer = await conn.execute(text('SELECT version()'))
        # print(answer.first())
        return {'version': str(answer.first())}
