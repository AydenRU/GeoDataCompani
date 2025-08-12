import json
from fastapi import HTTPException
from redis import Redis
from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.organizations_repositories import OrganizationsSelectDB

from app.schemas.schemas import OrganizationsS
from app.schemas.schemas import Geolocator


class OrganizationGet:

    def __init__(self, session: AsyncSession, redis: Redis=None):
        self.session = session
        self.redis = redis

    async def get_organization_by_id(self, id: int) -> OrganizationsS | dict :
        """Получить информацию об организацию по ID и возвращает организацию"""
        repositories = OrganizationsSelectDB(self.session)
        answer = await self.redis.get(f'{id}')
        if answer:
            await self.redis.expire(f'{id}', 60)
            return json.loads(answer)

        answer = await repositories.info_organization_by_id(id)

        if not answer:
            raise HTTPException(status_code=404, detail='Данные не найдены')

        org_schema = OrganizationsS.model_validate(answer)
        await self.redis.set(f'{id}', org_schema.model_dump_json(), ex=60)

        return org_schema


    async def get_organization_by_type(self, type_org: str) -> list[OrganizationsS]:
        """Получить информацию об организациях по виду деятельности и возвращает организации
        при нахождении совпадений"""
        repositories = OrganizationsSelectDB(self.session)
        answer = await self.redis.get(str(type_org))
        if answer:
            await self.redis.expire(str(type_org), 60)
            return [OrganizationsS.model_validate(i) for i in json.loads(answer)]

        answer = await repositories.info_organization_by_type(type_org)

        if not answer:
            raise HTTPException(status_code=404, detail='Данные не найдены')
        org_schema = [OrganizationsS.model_validate(i) for i in answer]
        await self.redis.set(str(type_org), json.dumps(jsonable_encoder(org_schema)), ex=60)
        return org_schema


    async def get_organization_by_building_id(self, builders_id: int) -> list[OrganizationsS] | str:
        """
        Получить информацию об организациях в здании по ID этого здания
        """
        repositories = OrganizationsSelectDB(self.session)
        answer = await self.redis.get(str(builders_id))
        if answer:
            await self.redis.expire(str(builders_id), 60)
            return [OrganizationsS.model_validate(i) for i in json.loads(answer)]

        answer = await repositories.info_organization_by_building(builders_id)

        if not answer:
            raise HTTPException(status_code=404, detail='Данные не найдены')
        org_schema = [OrganizationsS.model_validate(i) for i in answer]
        await self.redis.set(str(builders_id), json.dumps(jsonable_encoder(org_schema)), ex=60)
        return org_schema


    async def get_organization_by_name(self, name: str) -> list[OrganizationsS] | str:
        """Получить информацию об организациях по введенному слову/букве и возвращает организации
        при нахождении совпадений"""
        repositories = OrganizationsSelectDB(self.session)
        answer = await self.redis.get(str(name))
        if answer:
            await self.redis.expire(str(name), 60)
            return [OrganizationsS.model_validate(i) for i in json.loads(answer)]

        answer = await repositories.info_organization_by_name(name)

        if not answer:
            raise HTTPException(status_code=404, detail='Данные не найдены')
        org_schema = [OrganizationsS.model_validate(i) for i in answer]
        await self.redis.set(str(name), json.dumps(jsonable_encoder(org_schema)), ex=60)
        return org_schema


    async def get_organization_by_geo(self, data: Geolocator) -> list[OrganizationsS] | str:
        """Получить информацию об организациях по заданным координатам и радиусу."""
        repositories = OrganizationsSelectDB(self.session)
        name = json.dumps(data.model_dump())
        answer = await self.redis.get(name)
        if answer:
            await self.redis.expire(name, 60)
            return [OrganizationsS.model_validate(i) for i in json.loads(answer)]

        answer = await repositories.info_organization_by_geo_radius(data)

        if not answer:
            raise HTTPException(status_code=404, detail='Данные не найдены')
        org_schema = [OrganizationsS.model_validate(i) for i in answer]
        await self.redis.set(name, json.dumps(jsonable_encoder(org_schema)), ex=60)
        return org_schema