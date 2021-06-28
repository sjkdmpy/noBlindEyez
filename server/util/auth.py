from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from dynaconf import settings
import jwt


JWT_SECRET = settings.JWT_SECRET


ph = PasswordHasher()


def hashPassword(password) -> str:
	hashed_password = ph.hash(password)
	return hashed_password


def verifyPassword(hashed, password) -> bool:
	try:
		if ph.verify(hashed, password):
			return True
	except VerifyMismatchError:
		return False


def generateJWTToken(user):
	encoded = jwt.encode(user, JWT_SECRET, algorithm="HS256")
	return encoded


def decodeJWTToken(token):
	decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
	return decoded
