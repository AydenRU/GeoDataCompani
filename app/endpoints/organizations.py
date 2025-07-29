from fastapi import APIRouter
from fastapi import Request, HTTPException


from app.services.organizations import (get_organization_by_id,
                                        get_organization_by_type,
                                        get_organization_by_building_id,
                                        get_organization_by_name)

from app.repositories.select import info_organization_by_id

from app.schemas.schemas import OrganizationsS

router_organizations = APIRouter(prefix='/organizations', tags=['get_organization'])


@router_organizations.get('/{id_organization}')
async def get_organization_by_id_endpoint(id_organization: int, request: Request) -> OrganizationsS:
    try:
        return await get_organization_by_id(id_organization, request)
    except HTTPException as error:
        raise error


@router_organizations.get('/activity/{type_org}')
async def get_organization_by_type_endpoint(type_org: str, request:Request) -> list[OrganizationsS]:
    try:
        return await get_organization_by_type(type_org, request)
    except HTTPException as error:
        raise error


@router_organizations.get('/building/{builders_id}')
async def get_organization_by_building_id_endpoint(builders_id: int, request:Request) -> list[OrganizationsS]:
    try:
        return await get_organization_by_building_id(builders_id, request)
    except HTTPException as error:
        raise error


@router_organizations.get('/search/name/{name}')
async def get_organization_by_name_endpoint(name: str, request:Request) -> list[OrganizationsS]:
    try:
        return await get_organization_by_name(name, request)
    except HTTPException as error:
        raise error