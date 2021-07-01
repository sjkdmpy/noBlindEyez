from pydantic import BaseModel, validator


class IRIncident(BaseModel):
	title: str
	description: str
	location: int
	user: int

	@validator("title")
	def title_length(cls, value):
		if not len(value) >= 10:
			raise ValueError("title/minimum-10-characters")
		return value

	@validator("description")
	def description_length(cls, value):
		if not len(value) >= 20:
			raise ValueError("description/minimum-20-characters")
		return value
	