from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_organizations_repositories import UserOrganizationsDB

from app.schemas.schemas import OrganizationsS

class UserOrganizationsServices:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_list_organization(self, data):

        database =  UserOrganizationsDB(self.session)

        answer = await database.get_list_organization_db(data)

        if not answer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return [OrganizationsS.model_validate(i) for i in answer]