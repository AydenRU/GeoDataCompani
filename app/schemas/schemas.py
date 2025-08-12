from pydantic import BaseModel, Field, ConfigDict

from typing import Optional

class OrganizationsS(BaseModel):
    id: int = Field(..., description='Уникальный номер организации')
    builders_id: Optional[int] = Field(..., description='Уникальный номер здания')
    name: str = Field(..., description='Имя организации')
    type_org: str = Field(..., description='Отрасль организации')

    model_config = ConfigDict(from_attributes=True)


class Geolocator(BaseModel):
    latitude: float = Field(..., description='Широта', le=90, ge=-90)
    longitude: float = Field(..., description='Долгота', le=180, ge=-180)
    radius: Optional[float] = Field(..., description='Радиус от точки координат')