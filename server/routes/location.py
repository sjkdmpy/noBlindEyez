from fastapi import APIRouter, HTTPException
from tortoise.exceptions import ValidationError
from operator import itemgetter
from server.models import (
	Location, 
	ILocation, 
	ILocationIn, 
	ILocationQuery
)
from server.util.geolocation import (
	address2coords
)
from server.schemas.location import IILocation
from typing import Optional


router = APIRouter()

# TODO: ADD UPDATE ENDPOINT

@router.post("/")
async def add_location(location: IILocation):
	try:
		address = location.dict().get("address")

		coordinates = await address2coords(address)

		if not coordinates:
			raise HTTPException(status_code=400, detail="address-could-not-be-resolved")

		location_object = {
			"address": address,
			"latitude": coordinates["latitude"],
			"longitude": coordinates["longitude"]
		}

		print("-"*30)
		print(location_object)

		new_location = await Location.create(**location_object)

	except ValidationError as e:
		raise HTTPException(status_code=400, detail=str(e))

	new_location = await ILocation.from_tortoise_orm(new_location)

	return {
		"location": new_location 
	}


@router.get("/")
async def get_locations():
	locations = await ILocationQuery.from_queryset(Location.all())
	return {
		"locations": locations
	}


@router.get("/{location_id}")
async def get_location(location_id: int):
	location = await Location.filter(id=location_id)
	if not len(location):
		raise HTTPException(status_code=404, detail="The location doesn't exist")
	
	location = await ILocation.from_tortoise_orm(location[0])

	return {
		"location": location
	}


@router.delete("/{location_id}")
async def delete_location(location_id: int):
	location = await Location.filter(id=location_id)
	if not len(location):
		raise HTTPException(status_code=404, detail="The location doesn't exist")
	
	await location[0].delete()

	return {
		"message": "location-deleted"
	}


# @router.put("/{location_id}")
# async def update_location(location_id: int):
# 	location = await Location.filter(id=location_id)
# 	if not len(location):
# 		raise HTTPException(status_code=404, detail="The location doesn't exist")
# 	pass