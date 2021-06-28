from tortoise.models import Model
from tortoise import fields
from tortoise.validators import MinLengthValidator
from tortoise.contrib.pydantic import pydantic_model_creator


class Location(Model):
	id = fields.BigIntField(pk=True)
	address = fields.TextField(validators=[MinLengthValidator(10)])
	coordinates = fields.TextField()

	class Meta:
		table = "Location"

	def __str__(self):
		return self.address


ILocation = pydantic_model_creator(Location, name="Location")