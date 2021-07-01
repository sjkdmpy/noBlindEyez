from tortoise.models import Model
from tortoise import fields
from tortoise.validators import MinLengthValidator
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from enum import Enum
from server.validators.custom import (
	validate_longitude,
	validate_latitude
)


class IncidentPictures(Model):
	id = fields.BigIntField(pk=True)
	file = fields.TextField()
	incident_id = fields.ForeignKeyField("models.Incident", related_name="incident", on_delete="CASCADE")

	class Meta:
		table = "IncidentPictures"

	def __str__(self):
		return f"Incident_{self.incident_id}_Pictures"


class Incident(Model):
	id           = fields.BigIntField(pk=True)
	title        = fields.CharField(max_length=250, validators=[MinLengthValidator(10)])
	description  = fields.TextField(validators=[MinLengthValidator(20)])
	created_at   = fields.DatetimeField(auto_now_add=True)
	location = fields.ForeignKeyField("models.Location", related_name="location", on_delete="CASCADE")	
	user = fields.ForeignKeyField("models.User", related_name="user", on_delete="CASCADE")

	class Meta:
		table = "Incident"

	def __str__(self):
		return self.title


class Location(Model):
	id = fields.BigIntField(pk=True)
	address = fields.TextField(validators=[MinLengthValidator(10)])
	lat = fields.FloatField(validators=[validate_latitude])
	lng = fields.FloatField(validators=[validate_longitude])

	class Meta:
		table = "Location"

	def __str__(self):
		return self.address



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


class UserType(str, Enum):
	NORMAL = "NORMAL"
	PILOT  = "PILOT"

class User(Model):
	"""
	User model to authenticate and have access to the application
	"""
	id            = fields.BigIntField(pk=True)
	username      = fields.CharField(max_length=20, unique=True)
	password      = fields.TextField()
	user_type     = fields.CharEnumField(UserType)
	created_at    = fields.DatetimeField(auto_now_add=True)
	unity_pilot   = fields.ManyToManyField("models.Unity", related_name="unity_pilot", on_delete="CASCADE")

	class Meta:
		table = "User"
		ordering = ["created_at"]

	# class PydanticMeta:
		# exclude = ("password",)

	def __str__(self):
		return self.username


IIncidentPictures = pydantic_model_creator(IncidentPictures, name="IncidentPictures")
IIncidentPicturesIn = pydantic_model_creator(IncidentPictures, name="IncidentPicturesIn", exclude_readonly=True)
IIncidentPicturesQuery = pydantic_queryset_creator(IncidentPictures)


IIncident = pydantic_model_creator(Incident, name="Incident")
IIncidentIn = pydantic_model_creator(Incident, name="IncidentIn", exclude_readonly=True)
IIncidentQuery = pydantic_queryset_creator(Incident)


ILocation = pydantic_model_creator(Location, name="Location")
ILocationIn = pydantic_model_creator(Location, name="LocationIn", exclude_readonly=True)
ILocationQuery = pydantic_queryset_creator(Location)


IUnity = pydantic_model_creator(Unity, name="Unity")
IUnityIn = pydantic_model_creator(Unity, name="UnityIn", exclude_readonly=True)
IUnityQuery = pydantic_queryset_creator(Unity)


IUser= pydantic_model_creator(User, name="User")
IUserIn = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
IUserQuery = pydantic_queryset_creator(User)
