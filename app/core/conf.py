import os
import dotenv

dotenv.load_dotenv()

class SettingDB:
    def __init__(self):
        self.username_db = os.getenv('USERNAME_DB')
        self.host_db = os.getenv('HOST_DB')
        self.passwort_db = os.getenv('PASSWORD_DB')
        self.port_db = os.getenv('PORT_DB')
        self.name_db = os.getenv('POSTGRES_DB')

    def async_address_URL_DB(self):
        return f'postgresql+asyncpg://{self.username_db}:{self.passwort_db}@{self.host_db}:{self.port_db}/{self.name_db}'

setting_db = SettingDB()