from pydantic import BaseModel


class IAuthLogin(BaseModel):
	username: str
	password: str
