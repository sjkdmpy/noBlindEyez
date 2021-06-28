from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from operator import itemgetter
from server.models import User, IUserIn, IUser
from server.util.auth import (
	verifyPassword,
	generateJWTToken
)
from server.schemas.auth import IAuthLogin


router = APIRouter()


@router.post("/")
async def login(request: Request, user: IAuthLogin):
	username, password = itemgetter("username", "password")(user.dict())
	db_user = await User.filter(username=username)
	if not len(db_user):
		raise HTTPException(404, detail="user/does-not-exist")

	db_user = await IUser.from_tortoise_orm(db_user[0])
	db_user = db_user.dict()

	hashed_password = db_user.get("password")

	if not verifyPassword(hashed_password, password):
		raise HTTPException(400, detail="invalid-credentials")

	token = generateJWTToken({
		"id": db_user.get("id"),
		"username": username,
		"user_type": db_user.get("user_type"),
	})

	print("---------------")
	print(request)
	request.state.user = "Holi"

	return {
		"token": token
	}