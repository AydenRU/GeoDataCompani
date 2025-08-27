from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column, relationship
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

    builder: Mapped["BuildersOrm"] = relationship(back_populates="organizations")

    user: Mapped['UserOrm'] = relationship(back_populates='organizations', secondary='user_and_organizations')


class BuildersOrm(Base):
    __tablename__ = 'builders'

    id: Mapped[int] = mapped_column(primary_key=True)
    geolocations: Mapped[Geometry] = mapped_column(Geometry(geometry_type='POLYGON', srid=4326))

    organizations: Mapped["OrganizationsOrm"] = relationship(back_populates="builder",
                                                             cascade='all, delete')
