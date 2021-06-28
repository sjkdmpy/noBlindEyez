from fastapi import APIRouter, HTTPException
from server.models import User
from server.models import IUser, IUserIn, IUserQuery
from server.util.auth import hashPassword, verifyPassword
from operator import itemgetter


router = APIRouter()


@router.post("/", status_code=201)
async def create_user(user: IUserIn):
	username, password, user_type = itemgetter("username", "password", "user_type")(user.dict())
	hashed_password = hashPassword(password)
	user_dict = {
		"username": username,
		"password": hashed_password,
		"user_type": user_type
	}
	new_user = await User.create(**user_dict)
	return await IUser.from_tortoise_orm(new_user)
	

@router.get("/{user_id}")
async def get_user(user_id: int):
	user = await User.filter(id=user_id)
	if not len(user):
		raise HTTPException(status_code=404, detail="user/does-not-exist")

	user = await IUser.from_tortoise_orm(user[0])

	return user


@router.get("/")
async def get_users():
	users = await IUserQuery.from_queryset(User.all())
	return users


@router.delete("/{user_id}")
async def delete_user(user_id: int):
	user = await User.filter(id=user_id)
	if not len(user):
		raise HTTPException(status_code=404, detail="user/does-not-exist")

	await user[0].delete()
	
	return {
		"message": "user/deleted"
	}
