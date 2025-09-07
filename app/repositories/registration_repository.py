from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.registration import RegistrationUser
from app.models.user import UserOrm


class RegistrationDb:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_new_accaunt(self, data: RegistrationUser):
        """Добавление нового пользователя в БД
        :param data:
        :return:
        """
        user = UserOrm(**data.model_dump())
        self.session.add(user)
        try:
            await self.session.commit()
        except Exception as error:
            raise error

        return True
