from tortoise.validators import Validator
from tortoise.exceptions import ValidationError


def validate_latitude(value: float):
	"""
	Validate latitude value
	"""
	if not (-90 <= value <= 90):
		raise ValidationError(f"{value} is not a valid latitude value")


def validate_longitude(value: float):
	"""
	Validate longitude value
	"""
	if not (-180 <= value <= 180):
		raise ValidationError(f"{value}, is not a valid longitude value")