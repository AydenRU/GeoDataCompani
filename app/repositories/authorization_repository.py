from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from app.schemas.login import AuthorisationUser
from app.models.user import UserOrm

class AuthorizationDb:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_data_user_db(self, data: AuthorisationUser):
        """"""
        query = select(UserOrm).where(UserOrm.username == data.username)
        answer = await self.session.execute(query)
        answer = answer.scalar_one_or_none()
        print(answer)
        return answer
