from fastapi import HTTPException

from typing import Any, Coroutine


from app.repositories.select import (info_organization_by_id,
                                     info_organization_by_type,
                                     info_organization_by_building,
                                     info_organization_by_name)

from fastapi import Request
from app.schemas.schemas import OrganizationsS, OrganizationsSType


async def get_organization_by_id(id: int, request: Request) -> OrganizationsS:
    answer = await info_organization_by_id(id, request.app.state.session_db)

    if not answer:
        raise HTTPException(status_code=404, detail='Данные не найдены')

    org_schema = OrganizationsS.model_validate(answer)
    return org_schema


async def get_organization_by_type(type_org: str, request: Request) -> list[OrganizationsS]:
    answer = await info_organization_by_type(type_org, request.app.state.session_db)

    if not answer:
        raise HTTPException(status_code=404, detail='Данные не найдены')

    org_schema = [OrganizationsS.model_validate( i) for i in answer]
    return org_schema


async def get_organization_by_building_id(builders_id: int, request: Request) -> list[OrganizationsS]:
    answer = await info_organization_by_building(builders_id, request.app.state.session_db)

    if not answer:
        raise HTTPException(status_code=404, detail='Данные не найдены')

    org_schema = [OrganizationsS.model_validate( i) for i in answer]
    return org_schema



async def get_organization_by_name(name: str, request: Request) -> list[OrganizationsS]:
    answer = await info_organization_by_name(name, request.app.state.session_db)

    if not answer:
        raise HTTPException(status_code=404, detail='Данные не найдены')

    org_schema = [OrganizationsS.model_validate(i) for i in answer]
    return org_schema
