from pydantic import BaseModel, Field

from typing import Optional, Annotated

class OrganizationsS(BaseModel):
    id: int
    builders_id: Optional[int]
    name: str
    type_org: str

    model_config = {
        "from_attributes": True
    }

class OrganizationsSId(BaseModel):
    id: int

class OrganizationsSType(BaseModel):
    type_org: str

class BuildingSId(BaseModel):
    id: int


class Geolocator(BaseModel):
    latitude: float
    longitude: float
    radius: Optional[float]