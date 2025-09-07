from authx import AuthX, AuthXConfig
from fastapi import Request, HTTPException, status
import jwt


config = AuthXConfig(JWT_SECRET_KEY='hi_man',
                     JWT_ACCESS_COOKIE_NAME='my_cookies',
                     JWT_TOKEN_LOCATION=['cookies'])

auth = AuthX(config)


async def check_access_token(request: Request):
    """Проверка JWT-токена"""
    try:
        a = request.cookies.get('my_cookies')
        data = jwt.decode(a, key=config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
        print(data)
        return data
    except Exception as error:
        print(error)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Устаревший токен')