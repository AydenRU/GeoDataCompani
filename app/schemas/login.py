from pydantic import BaseModel

class AuthorisationUser(BaseModel):

    username: str
    password: str