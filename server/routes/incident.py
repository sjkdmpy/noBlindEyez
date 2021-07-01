from fastapi import APIRouter, HTTPException
from tortoise.query_utils import Q
from server.models import (
	Incident, 
	IIncident, 
	IIncidentQuery,
	Location,
	User
)
from server.schemas.incident import IRIncident
from operator import itemgetter
from typing import Optional


router = APIRouter()

# TODO: When middleware's ready, the request
# will have the user_id
@router.post("/", status_code=201)
async def add_incident(incident: IRIncident):
	title, description, location, user = itemgetter("title", "description", "location", "user")(incident.dict())
	
	location = await Location.filter(id=location)
	
	if not len(location):
		raise HTTPException(status_code=400, detail="location/does-not-exist")

	user = await User.filter(id=user)

	if not len(user):
		raise HTTPException(status_code=400, detail="user/does-not-exist")

	new_incident = await Incident.create(**{
		"title": title,
		"description": description,
		"location": location[0],
		"user": user[0]
	})

	new_incident = await IIncident.from_tortoise_orm(new_incident)	

	return {
		"incident": new_incident
	}


@router.get("/")
async def get_incidents(q: Optional[str] = None, page: int = 1, records: int = 10):
	if q:
		incidents = await IIncidentQuery.from_queryset(Incident.filter(
			Q(title__startswith=q) |
			Q(description__startswith=q)
		))
	else:
		incidents = await IIncidentQuery.from_queryset(Incident.all().order_by("created_at").limit(records).offset((page-1)*records))
	return  {
		"incidents": incidents
	}


@router.get("/{incident_id}")
async def get_incident(incident_id: int):
	incident = await Incident.filter(id=incident_id)
	
	if not len(incident):
		raise HTTPException(status_code=400, detail="incident/does-not-exist")

	incident = await IIncident.from_tortoise_orm(incident[0])

	return incident


@router.delete("/{incident_id}")
async def delete_incident(incident_id: int):
	incident = await Incident.filter(id=incident_id)

	if not len(incident):
		raise HTTPException(status_code=400, detail="incident/does-not-exist")

	await incident[0].delete()

	return {
		"message": "incident/deleted"
	}


@router.get("/search")
async def search_nearby_incidents():
	pass