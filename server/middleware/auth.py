from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):
	"""
	Verify if the request is authenticated for protected endpoints
	"""
	async def dispatch(self, request, call_next):
		response = await call_next(request)
		# print(request.state.user)
		return response


class UserKeeper(BaseHTTPMiddleware):
	"""
	Verify if the current user has permission to the given endpoint
	"""
	async def dispatch(self, request, call_next):
		response = await call_next(request)
		return response