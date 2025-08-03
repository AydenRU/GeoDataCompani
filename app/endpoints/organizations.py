from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.params import Depends

from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.session import get_session
from app.services.organizations import OrganizationGet
from app.schemas.schemas import OrganizationsS, Geolocator

router_organizations = APIRouter(prefix='/organizations', tags=['get_organization'])


@router_organizations.get('/{id_organization}')
async def get_organization_by_id_endpoint(id_organization: int,
                                          services: Annotated[AsyncSession, Depends(get_session)]) -> OrganizationsS:
    try:
        services = OrganizationGet(services)
        return await services.get_organization_by_id(id_organization)
    except HTTPException as error:
        raise error


@router_organizations.get('/activity/{type_org}')
async def get_organization_by_type_endpoint(type_org: str,
                                            services: Annotated[AsyncSession, Depends(get_session)]) -> list[OrganizationsS]:
    try:
        services = OrganizationGet(services)
        return await services.get_organization_by_type(type_org)
    except HTTPException as error:
        raise error


@router_organizations.get('/building/{builders_id}')
async def get_organization_by_building_id_endpoint(builders_id: int,
                                                   services: Annotated[AsyncSession, Depends(get_session)]) -> list[OrganizationsS]:
    try:
        services = OrganizationGet(services)
        return await services.get_organization_by_building_id(builders_id)
    except HTTPException as error:
        raise error


@router_organizations.get('/search/name/{name}')
async def get_organization_by_name_endpoint(name: str, services: Annotated[AsyncSession, Depends(get_session)]) -> list[OrganizationsS]:
    try:
        services = OrganizationGet(services)
        return await services.get_organization_by_name(name)
    except HTTPException as error:
        raise error


@router_organizations.post('/search/geo')
async def get_organization_by_geo_endpoint(data: Geolocator,
                                           services: Annotated[AsyncSession, Depends(get_session)]) -> list[OrganizationsS]:
    try:
        services = OrganizationGet(services)
        return await services.get_organization_by_geo(data)
    except HTTPException as error:
        raise error
