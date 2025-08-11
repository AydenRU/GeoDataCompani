from fastapi import Request

from typing import AsyncGenerator

from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession


async def get_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    request = request.app.state.session_db

    async with request() as session:
        yield session

async def get_redis(request: Request) -> Redis:
    return request.app.state.redis

