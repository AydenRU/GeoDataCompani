from sqlalchemy.ext.asyncio import AsyncSession

from app.core.hash import my_hash
from app.repositories.registration_repository import RegistrationDb

class RegistrationServices:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def registration(self, data):
        """Метод обрабатывающий запрос добавления пользователя

        """
        db = RegistrationDb(self.session)
        try:
            data.password = my_hash.hash(data.password)
            await db.add_new_accaunt(data)
        except Exception as error:
            return error

        return True

