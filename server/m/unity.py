from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from enum import Enum


class UnityKind(str, Enum):
	AERIAL = "AERIAL"
	LAND   = "LAND"

class Unity(Model):
	id = fields.BigIntField(pk=True)
	name = fields.CharField(max_length=100, unique=True, validators=[])
	active = fields.BooleanField(default=False)
	kind = fields.CharEnumField(UnityKind)

	class Meta:
		table = "Unity"
	
	def __str__(self):
		return self.name

IUnity = pydantic_model_creator(Unity, name="Unity")