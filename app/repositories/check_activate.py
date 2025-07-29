from sqlalchemy.orm import Mapped

from sqlalchemy import  text


async def check_connection_db(create_db):
    """Проверка подключения к БД"""
    async with create_db() as session_db:
        answer = await session_db.execute(text('SELECT 1'))

        return {'version': str(answer.first())}