import uvicorn
from dynaconf import settings


PORT = settings.PORT
HOST = settings.HOST


if __name__ == "__main__":
	uvicorn.run("server.index:app", host=HOST, port=PORT, log_level="info", reload=True)