from typing import Any, Coroutine, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, join, Row, RowMapping
from sqlalchemy.orm import joinedload

from app.models.user import UserOrganizationsOrm
from app.models.organizations import OrganizationsOrm

class UserOrganizationsDB:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_list_organization_db(self, data: dict) -> list[OrganizationsOrm]:
        query = select(OrganizationsOrm).join(UserOrganizationsOrm).where(UserOrganizationsOrm.id_user == data['id'])

        answer = await self.session.execute(query)

        return answer.scalars().all()


