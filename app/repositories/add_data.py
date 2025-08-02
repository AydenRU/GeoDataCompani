from shapely.geometry import shape

from geoalchemy2.shape import from_shape

from app.models.models import BuildersOrm, OrganizationsOrm



class AddOrm:

    @staticmethod
    async def loading_builds(data: list, session_db):

        async with session_db() as session:
            # Загрузим здания
            for b in data:
                polygon = shape(b["geolocations"])
                builder = BuildersOrm(geolocations=from_shape(polygon, srid=4326))
                session.add(builder)

            await session.commit()


    @staticmethod
    async def loading_organizations(data: list, session_db):

        async with session_db() as session:
            for o in data:
                point = shape(o["geolocations"])
                org = OrganizationsOrm(
                    name=o["name"],
                    type_org=o["type_org"],
                    geolocations=from_shape(point, srid=4326),
                    builders_id=o["builders_id"]
                )
                session.add(org)

            await session.commit()