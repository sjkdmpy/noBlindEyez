from pydantic import BaseModel


class IILocation(BaseModel):
	address: str