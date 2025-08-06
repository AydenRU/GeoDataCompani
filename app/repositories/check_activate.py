from sqlalchemy import select, literal_column
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.organizations import BuildersOrm

class CheckDb:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def check_connection_db(self) -> dict:
        """Проверка подключения к БД
        Args:
            self.session: Сессия подключение к БД
        Return:
            Вернет dict:
                {'version': 1}
        """

        answer = await self.session.execute(select(literal_column('1')))

        return {'version': str(answer.first())}

    @staticmethod
    async def check_empy_data_db(session: AsyncSession):
        """Проверка на наличие данных в БД
        Args:
            session: Сессия подключение к БД
        Return:
            True, если данные в БД есть, иначе False
        """
        answer = await session.execute(select(BuildersOrm).limit(1))

        answer = answer.scalars().first()

        return True if answer else False