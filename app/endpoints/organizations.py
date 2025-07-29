from fastapi import APIRouter
from fastapi import Request


from app.repositories.select import info_organization_by_id

from app.schemas.schemas import OrganizationsSId, OrganizationsS

router_organizations = APIRouter(prefix='/organizations', tags=['get_organization'])


@router_organizations.get('/{id_organization}')
async def get_organization_by_id(id: int, request: Request) -> OrganizationsS:
    answer = await info_organization_by_id(id, request.app.state.session_db)

    org_schema = OrganizationsS.model_validate(answer)
    return org_schema
