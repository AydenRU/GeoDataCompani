from typing import AsyncGenerator

from fastapi import APIRouter
from fastapi import Request, HTTPException
from fastapi.params import Depends

from typing import Annotated

from app.services.organizations import OrganizationGet

# from app.repositories.organizations_repositories import

from app.schemas.schemas import OrganizationsS, Geolocator
from sqlalchemy.ext.asyncio import AsyncSession

router_organizations = APIRouter(prefix='/organizations', tags=['get_organization'])

async def get_session(request: Request) -> AsyncGenerator[OrganizationGet, None]:
    sessionmaker = request.app.state.session_db
    async with sessionmaker() as session:
        yield OrganizationGet(session)


@router_organizations.get('/{id_organization}')
async def get_organization_by_id_endpoint(id_organization: int, services: Annotated[OrganizationGet, Depends(get_session)]) -> OrganizationsS:
    try:
        return await services.get_organization_by_id(id_organization)
    except HTTPException as error:
        raise error


@router_organizations.get('/activity/{type_org}')
async def get_organization_by_type_endpoint(type_org: str, services: Annotated[OrganizationGet, Depends(get_session)]) -> list[OrganizationsS]:
    try:
        return await services.get_organization_by_type(type_org)
    except HTTPException as error:
        raise error


@router_organizations.get('/building/{builders_id}')
async def get_organization_by_building_id_endpoint(builders_id: int, services: Annotated[OrganizationGet, Depends(get_session)]) -> list[OrganizationsS]:
    try:
        return await services.get_organization_by_building_id(builders_id)
    except HTTPException as error:
        raise error


@router_organizations.get('/search/name/{name}')
async def get_organization_by_name_endpoint(name: str, services: Annotated[OrganizationGet, Depends(get_session)]) -> list[OrganizationsS]:
    try:
        return await services.get_organization_by_name(name)
    except HTTPException as error:
        raise error


@router_organizations.post('/search/geo')
async def get_organization_by_geo_endpoint(data: Geolocator, services: Annotated[OrganizationGet, Depends(get_session)]) -> list[OrganizationsS]:
    try:
        return await services.get_organization_by_geo(data)
    except HTTPException as error:
        raise error