from fastapi import APIRouter, status
from fastapi import HTTPException
from fastapi.params import Depends

from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.session import get_session, get_redis
from app.services.organizations import OrganizationGet
from app.schemas.schemas import OrganizationsS, Geolocator

from redis.asyncio import Redis

router_organizations = APIRouter(prefix='/organizations', tags=['get_organization'])


@router_organizations.get('/{id_organization}',
                          response_model=OrganizationsS,
                          status_code=status.HTTP_200_OK,
                          summary='Получить информацию об организацию по ID')
async def get_organization_by_id_endpoint(id_organization: int,
                                          services: Annotated[AsyncSession, Depends(get_session)],
                                          redis: Annotated[Redis, Depends(get_redis)]) -> OrganizationsS:
    """
    Получить информацию об организацию по ID и возвращает организацию
    Args:
        id_organization: ID организации.
        services: AsyncSession
        conn_redis: Radis
    Return:
        OrganizationsS - информация об организации
    Raise:
        HTTPException если данные не найдены вернёт 404
    """

    try:
        services = OrganizationGet(services, redis)
        return await services.get_organization_by_id(id_organization)
    except HTTPException as error:
        raise error


@router_organizations.get('/activity/{type_org}',
                          response_model=list[OrganizationsS],
                          status_code=status.HTTP_200_OK,
                          summary='Получить информацию об организации по виду деятельности')
async def get_organization_by_type_endpoint(type_org: str,
                                            services: Annotated[AsyncSession, Depends(get_session)]) -> list[OrganizationsS]:
    """
    Получить информацию об организациях по виду деятельности и возвращает организации
    при нахождении совпадений
    Args:
        type_org: Вид деятельности
        services: AsyncSession
    Return:
        list[OrganizationsS] - информация об организации
    Raise:
        HTTPException если данные не найдены вернёт 404
    """
    try:
        services = OrganizationGet(services)
        return await services.get_organization_by_type(type_org)
    except HTTPException as error:
        raise error


@router_organizations.get('/building/{builders_id}',
                          response_model=list[OrganizationsS],
                          status_code=status.HTTP_200_OK,
                          summary='Получить информацию об организациях по ID здания')
async def get_organization_by_building_id_endpoint(builders_id: int,
                                                   services: Annotated[AsyncSession, Depends(get_session)]) -> list[OrganizationsS]:
    """
    Получить информацию об организациях в здании по ID этого здания
    Args:
        builders_id: ID здания
        services: AsyncSession
    Return:
        list[OrganizationsS] - информация об организации\ю
    Raise:
        HTTPException если данные не найдены вернёт 404
    """
    try:
        services = OrganizationGet(services)
        return await services.get_organization_by_building_id(builders_id)
    except HTTPException as error:
        raise error


@router_organizations.get('/search/name/{name}',
                          response_model=list[OrganizationsS],
                          status_code=status.HTTP_200_OK,
                          summary='Получить информацию об организациях по введенному слову/букве ')
async def get_organization_by_name_endpoint(name: str,
                                            services: Annotated[AsyncSession, Depends(get_session)]) -> list[OrganizationsS]:
    """
    Получить информацию об организациях по введенному слову/букве и возвращает организации
    при нахождении совпадений
    Args:
        name: ID здания
        services: AsyncSession
    Return:
        list[OrganizationsS] - информация об организации\ях
    Raise:
        HTTPException если данные не найдены вернёт 404
    """
    try:
        services = OrganizationGet(services)
        return await services.get_organization_by_name(name)
    except HTTPException as error:
        raise error


@router_organizations.post('/search/geo',
                           response_model=list[OrganizationsS],
                           status_code=status.HTTP_200_OK,
                           summary='Получить информацию об организация по заданным координатам и радиусом')
async def get_organization_by_geo_endpoint(data: Geolocator,
                                           services: Annotated[AsyncSession, Depends(get_session)]) -> list[OrganizationsS]:
    """
    Получить информацию об организациях по заданным координатам и радиусу.
    Args:
        data:
            latitude: Широта
            longitude: Долгота
            radius: Радиус поиска
        services: AsyncSession
    Return:
        list[OrganizationsS] - информация об организации\ях
    Raise:
        HTTPException если данные не найдены вернёт 404
    """
    try:
        services = OrganizationGet(services)
        return await services.get_organization_by_geo(data)
    except HTTPException as error:
        raise error
