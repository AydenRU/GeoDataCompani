from sqlalchemy import Table, Column, MetaData
from sqlalchemy import  Integer, String

from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column
from sqlalchemy import  ForeignKey
from geoalchemy2 import Geometry


class Base(DeclarativeBase):
    pass


class OrganizationsOrm(Base):
    __tablename__ = 'organizations'

    id: Mapped[int] = mapped_column(primary_key=True)
    builders_id: Mapped[int | None] = mapped_column(ForeignKey('builders.id'))
    name: Mapped[str | None]
    geolocations: Mapped[Geometry] = mapped_column(Geometry(geometry_type='POINT', srid=4326))
    type_org: Mapped[str]


class BuildersOrm(Base):
    __tablename__ = 'builders'

    id: Mapped[int] = mapped_column(primary_key=True)
    geolocations: Mapped[Geometry] = mapped_column(Geometry(geometry_type='POLYGON', srid=4326))
