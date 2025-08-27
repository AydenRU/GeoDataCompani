from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.organizations import Base

class UserOrm(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    organizations: Mapped[list['OrganizationsOrm']] = relationship( back_populates='user' ,secondary='user_and_organizations')


class UserOrganizationsOrm(Base):
    __tablename__ = 'user_and_organizations'

    id_user: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete='CASCADE'), primary_key=True)

    id_organization: Mapped[int] = mapped_column(ForeignKey('organizations.id', ondelete='CASCADE'), primary_key=True)