from tortoise.models import Model
from tortoise import fields
from tortoise.validators import MinLengthValidator
from tortoise.contrib.pydantic import pydantic_model_creator


class Incident(Model):
	id           = fields.BigIntField(pk=True)
	title        = fields.CharField(max_length=250, validators=[MinLengthValidator(10)])
	description  = fields.TextField(validators=[MinLengthValidator(20)])
	created_at   = fields.DatetimeField(auto_now_add=True)
	location_id  = fields.ForeignKeyField(".location.Location", related_name="location", on_delete="CASCADE")	
	user_id      = fields.ForeignKeyField("user.User", related_name="user", on_delete="CASCADE")

	class Meta:
		table = "Incident"

	def __str__(self):
		return self.title


IIncident = pydantic_model_creator(Incident, name="Incident")