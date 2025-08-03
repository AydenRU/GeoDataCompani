from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from geoalchemy2 import Geometry

from app.models.models import OrganizationsOrm

from app.schemas.schemas import Geolocator



class OrganizationsSelectDB:

    def __init__(self, session: AsyncSession):
        self.db_session = session


    async def info_organization_by_id(self, id: int) -> tuple:

        stmt = select(OrganizationsOrm).where(OrganizationsOrm.id == id)

        answer = await self.db_session.execute(stmt)

        org = answer.scalar_one_or_none()
        return org



    async def info_organization_by_type(self, type_org: str) -> list:

        stmt = select(OrganizationsOrm).where(OrganizationsOrm.type_org == type_org)
        answer = await  self.db_session.execute(stmt)

        org = answer.scalars().all()

        return org



    async def info_organization_by_building(self, builders_id: int) -> list:

        stmt = select(OrganizationsOrm).where(OrganizationsOrm.builders_id == builders_id)
        answer = await self.db_session.execute(stmt)

        org = answer.scalars().all()

        return org



    async def info_organization_by_name(self, name: str) -> list:

        stmt = select(OrganizationsOrm).where(OrganizationsOrm.name.like(f"%{name}%"))
        answer = await self.db_session.execute(stmt, {'name' : f"%{name}%"})

        org = answer.scalars().all()

        return org


    async def info_organization_by_geo_radius(self, data: Geolocator) -> list:

        stmt = (
            select(OrganizationsOrm)
            .where(
                func.ST_DWithin(
                    OrganizationsOrm.geolocations,
                    func.ST_SetSRID(
                        func.ST_MakePoint(data.longitude, data.latitude), 4326).cast(Geometry),
                    data.radius
                )
            )
        )

        answer = await self.db_session.execute(stmt, {"longitude" : data.longitude,
                                           "latitude": data.latitude,
                                           "radius" : data.radius}
                                        )
        org = answer.scalars().all()

        return org