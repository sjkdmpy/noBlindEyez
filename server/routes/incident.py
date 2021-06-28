from fastapi import APIRouter, HTTPException
from server.models import (
	Incident, 
	IIncident, 
	IIncidentIn
)


router = APIRouter()


@router.post("/")
async def add_incident(incident: IIncidentIn):
	new_incident = 3


@router.get("/")
async def get_incidents():
	pass


@router.get("/{incident_id}")
async def get_incident(incident_id: int):
	pass


@router.delete("/{incident_id}")
async def delete_incident(incident_id: int):
	pass