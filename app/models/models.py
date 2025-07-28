from sqlalchemy import Table, Column, MetaData
from sqlalchemy import  Integer, String

from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserOrm(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str] = mapped_column()













# metadata_db = MetaData()
#
# users = Table(
#     'users',
#     metadata_db,
#     Column('id', Integer, primary_key=True),
#     Column('name', String)
# )