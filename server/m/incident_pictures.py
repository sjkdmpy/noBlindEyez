from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class IncidentPictures(Model):
	id = fields.BigIntField(pk=True)
	file = fields.TextField()
	incident_id = fields.ForeignKeyField("incident.Incident", related_name="incident", on_delete="CASCADE")

	class Meta:
		table = "IncidentPictures"

	def __str__(self):
		return f"Incident_{self.incident_id}_Pictures"
		

IIncidentPictures = pydantic_model_creator(IncidentPictures, name="IncidentPictures")
