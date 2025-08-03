from fastapi import Request

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession


async def get_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    request = request.app.state.session_db

    async with request() as session:
        yield session
