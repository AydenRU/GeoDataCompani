import redis.asyncio as async_redis
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingDB(BaseSettings):
    username_db: str = Field('postgres', alias='USERNAME_DB')
    password_db: str = Field('postgres', alias='PASSWORD_DB')
    host_db: str = Field('localhost', alias='HOST_DB')
    port_db: int = Field(5432, alias='PORT_DB')
    name_db: str = Field('postgres', alias='POSTGRES_DB')

    model_config  = SettingsConfigDict(env_file='.env',
                                       extra="ignore")

    def async_address_URL_DB(self):
        return f'postgresql+asyncpg://{self.username_db}:{self.password_db}@{self.host_db}:{self.port_db}/{self.name_db}'


class SettingRedis(BaseSettings):
    host_redis: str = Field('localhost', alias='HOST_REDIS')
    port_redis: int = Field(6379, alias='PORT_REDIS')

    model_config = SettingsConfigDict(env_file='.env',
                                      extra="ignore")

    def async_connection_redis(self):
        return async_redis.Redis(host=self.host_redis, port=self.port_redis, decode_responses=True)


setting_db = SettingDB()

setting_redis = SettingRedis()

