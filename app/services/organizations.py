from fastapi import HTTPException

from typing import Any, Coroutine

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.organizations_repositories import OrganizationsSelectDB

from fastapi import Request
from app.schemas.schemas import OrganizationsS
from app.schemas.schemas import Geolocator


class OrganizationGet:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_organization_by_id(self, id: int) -> OrganizationsS:
        repositories = OrganizationsSelectDB(self.session)

        answer = await repositories.info_organization_by_id(id)

        if not answer:
            raise HTTPException(status_code=404, detail='Данные не найдены')

        org_schema = OrganizationsS.model_validate(answer)
        return org_schema


    async def get_organization_by_type(self, type_org: str) -> list[OrganizationsS]:
        repositories = OrganizationsSelectDB(self.session)

        answer = await repositories.info_organization_by_type(type_org)

        if not answer:
            raise HTTPException(status_code=404, detail='Данные не найдены')

        org_schema = [OrganizationsS.model_validate(i) for i in answer]
        return org_schema


    async def get_organization_by_building_id(self, builders_id: int) -> list[OrganizationsS]:
        repositories = OrganizationsSelectDB(self.session)

        answer = await repositories.info_organization_by_building(builders_id)

        if not answer:
            raise HTTPException(status_code=404, detail='Данные не найдены')

        org_schema = [OrganizationsS.model_validate(i) for i in answer]
        return org_schema


    async def get_organization_by_name(self, name: str) -> list[OrganizationsS]:
        repositories = OrganizationsSelectDB(self.session)

        answer = await repositories.info_organization_by_name(name)

        if not answer:
            raise HTTPException(status_code=404, detail='Данные не найдены')

        org_schema = [OrganizationsS.model_validate(i) for i in answer]
        return org_schema


    async def get_organization_by_geo(self, data: Geolocator):
        repositories = OrganizationsSelectDB(self.session)

        answer = await repositories.info_organization_by_geo_radius(data)

        if not answer:
            raise HTTPException(status_code=404, detail='Данные не найдены')

        org_schema = [OrganizationsS.model_validate(i) for i in answer]
        return org_schema
