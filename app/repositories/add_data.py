from shapely.geometry import shape

from geoalchemy2.shape import from_shape
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.organizations import BuildersOrm, OrganizationsOrm



class AddOrm:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def loading_builds(self, data: list):
        """Принимает список зданий и загружает в базу данных
        Args:
            data (list):
                id: уникальный номер здания
                geolocations: координаты
                    type: тип координат
                    coordinates: Координаты
        """

        for b in data:
            polygon = shape(b["geolocations"])
            builder = BuildersOrm(geolocations=from_shape(polygon, srid=4326))
            self.session.add(builder)

            await self.session .commit()


    async def loading_organizations(self, data: list):
        """Принимает список организаций и загружает в базу данных
        Args:
            data (list):
                id: уникальный номер здания
                builders_id: уникальный индентификатор здания, где располагается здание
                name: название организации
                type_org: вид деятельности организации
                geolocations: координаты
                    type: тип координат
                    coordinates: Координаты
        """

        for o in data:
            point = shape(o["geolocations"])
            org = OrganizationsOrm(
                name=o["name"],
                type_org=o["type_org"],
                geolocations=from_shape(point, srid=4326),
                builders_id=o["builders_id"]
            )
            self.session.add(org)

            await self.session .commit()