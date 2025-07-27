from sqlalchemy.orm import Mapped

from sqlalchemy import  text

from app.models.models import UserOrm


async def test(create_db):
    async with create_db() as session_db:
        answer = await session_db.execute(text('SELECT 1'))

        return {'version': str(answer.first())}