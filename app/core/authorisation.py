import os
import jwt
import dotenv

from authx import AuthX, AuthXConfig
from fastapi import Request, HTTPException, status

dotenv.load_dotenv()

config = AuthXConfig(JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY'),
                     JWT_ACCESS_COOKIE_NAME='my_cookies',
                     JWT_TOKEN_LOCATION=['cookies'])

auth = AuthX(config)

class CheckToken:

    @staticmethod
    async def check_access_token(request: Request):
        """Проверка JWT-токена"""
        token = request.cookies.get('my_cookies')
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Access token не найден')
        try:
            data = jwt.decode(token, key=config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
            return data
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Устаревший токен')

    @staticmethod
    async def check_refresh_token(request: Request):
        """Проверка JWT-токена"""
        token = request.cookies.get('jwt_refresh_token')
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Refresh token не найден')
        try:
            data = jwt.decode(token, key=config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
            return data
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Устаревший токен')

