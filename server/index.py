from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.middleware.auth import AuthMiddleware
from .routes import (
	user,
	auth,
	location,
	incident
)
from time import ctime


app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_methods=["*"],
	allow_headers=["*"]
)
app.add_middleware(AuthMiddleware)
# @app.middleware("http")
# async def authMiddleware(request: Request, call_next):
# 	print(request)
# 	print(request.json())
# 	response = await call_next(request)
# 	return response

# app.add_middleware(authMiddleware)

@app.get("/")
async def index():
	return { "time": ctime() }


# Register the API routes

app.include_router(
	user.router,
	prefix="/api/user",
	tags=["User"],
)

app.include_router(
	auth.router,
	prefix="/api/auth",
	tags=["Auth"]
)

app.include_router(
	location.router,
	prefix="/api/location",
	tags=["Location"]	
)

app.include_router(
	incident.router,
	prefix="/api/incident",
	tags=["Incident"]
)


# Connect to the database and create the schemas
# defined in models. Each time the schema changes,
# the tables are generated automatically.
register_tortoise(
	app,
	db_url="postgres://noblindeye:noblindeyez@localhost:5432/noblindeye",
	modules={"models": ["server.models"]},
	generate_schemas=True,							 # Overwrites models, if any change
	add_exception_handlers=True                                                                
)