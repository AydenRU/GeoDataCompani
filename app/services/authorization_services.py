from fastapi import HTTPException, status
from fastapi import Response
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from app.core.hash import my_hash
from app.core.authorisation import auth

from app.repositories.authorization_repository import AuthorizationDb

from app.schemas.login import AuthorisationUser
from app.schemas.users import UserS


class AuthorizationServices:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_data_user(self, data: AuthorisationUser, response: Response):

        repositories = AuthorizationDb(self.session)
        answer = await repositories.get_data_user_db(data)

        if not answer:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        orm_schema = UserS.model_validate(answer)

        if not my_hash.verify(data.password, orm_schema.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        access_token = auth.create_access_token(uid=str(orm_schema.id),
                                                data={'id': orm_schema.id},
                                                expiry=timedelta(minutes=1))
        refresh_token = auth.create_refresh_token(uid='jwt_refresh_token',
                                                  data={'id': orm_schema.id},
                                                  expiry=timedelta(minutes=10))

        response.set_cookie(key=auth.config.JWT_ACCESS_COOKIE_NAME, value=access_token, httponly=True)
        response.set_cookie(key='jwt_refresh_token', value=refresh_token, httponly=True)

        return [access_token, refresh_token]

    async def generation_new_access_token(self, data_refresh_token: dict, response: Response) -> str:
        """Генерация Access token"""

        access_token = auth.create_access_token(uid=str(data_refresh_token['id']),
                                                data={'id': data_refresh_token['id']},
                                                expiry=(timedelta(minutes=1)))

        response.set_cookie(key=auth.config.JWT_ACCESS_COOKIE_NAME,
                            value=access_token,
                            httponly=True)
        return access_token