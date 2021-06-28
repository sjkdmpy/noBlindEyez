from tortoise.models import Model
from tortoise import fields
from tortoise.signals import pre_save
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
	id = fields.BigIntField(pk=True)
	username = fields.CharField(max_length=20, unique=True)
	password = fields.CharField(max_length=23)
	created_at = fields.DatetimeField(auto_now_add=True)

	class Meta:
		table = "User"

	def __str__(self):
		return self.username


IUser= pydantic_model_creator(User, name="User")
IUserRO = pydantic_model_creator(User, name="IUser", exclude_readonly=True)