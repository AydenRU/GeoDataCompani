from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingDB(BaseSettings):
    username_db: str = Field('postgres', alias='USERNAME_DB')
    password_db: str = Field('postgres', alias='PASSWORD_DB')
    host_db: str = Field('localhost', alias='HOST_DB')
    port_db: int = Field(5432, alias='PORT_DB')
    name_db: str = Field('postgres', alias='POSTGRES_DB')

    model_config  = SettingsConfigDict(env_file='.env')


    def async_address_URL_DB(self):
        print(self.username_db)
        return f'postgresql+asyncpg://{self.username_db}:{self.password_db}@{self.host_db}:{self.port_db}/{self.name_db}'

setting_db = SettingDB()



    # def __init__(self):
    #     self.username_db = os.getenv('USERNAME_DB')
    #     self.host_db = os.getenv('HOST_DB')
    #     self.passwort_db = os.getenv('PASSWORD_DB')
    #     self.port_db = os.getenv('PORT_DB')
    #     self.name_db = os.getenv('POSTGRES_DB')
