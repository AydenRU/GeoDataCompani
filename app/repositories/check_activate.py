from sqlalchemy import select, literal_column
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import BuildersOrm

class CheckDb:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def check_connection_db(self):
        """Проверка подключения к БД"""

        answer = await self.session.execute(select(literal_column('1')))

        return {'version': str(answer.first())}

    @staticmethod
    async def check_empy_data_db(session: AsyncSession):

        answer = await session.execute(select(BuildersOrm).limit(1))

        answer = answer.scalars().first()
        print(answer)

        return True if answer else False