from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import OrganizationsOrm


async def info_organization_by_id(id: int, session: AsyncSession) -> tuple:

    async with session() as conn:
    #
    #     answer = await conn.execute("""
    #                                 SELECT * FROM organizations
    #                                     WHERE id = :id
    #                                 """, {'id': id})
    # answer = await answer.first()

        stmt = select(OrganizationsOrm).where(OrganizationsOrm.id == id)
        answer = await conn.execute(stmt)

    org = answer.scalar_one_or_none()
    return org


async def info_organization_by_type(type_org: int, session: AsyncSession) -> tuple:

    async with session() as conn:
        answer = await conn.execute("""
                                    SELECT * FROM organizations
                                        WHERE id = :id
                                    """, {'type_org': type_org})
    answer = await answer.all()

    return answer


async def info_building(id: int, session: AsyncSession) -> list:

    async with session() as conn:
        answer = await conn.execute("""
                                    SELECT * FROM organizations
                                        WHERE builders_id = :id
                                    """, {'id': id})
    answer = await answer.all()

    return answer