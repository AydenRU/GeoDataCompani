from authx import AuthX, AuthXConfig


config = AuthXConfig(JWT_SECRET_KEY='hi_man',
                     JWT_ACCESS_COOKIE_NAME='my_coolies_=)',
                     JWT_TOKEN_LOCATION=['cookies'])

auth = AuthX(config)
