from pydantic import BaseModel, Field, ConfigDict


class UserS(BaseModel):
    id: int
    username: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5)

    model_config = ConfigDict(from_attributes=True)