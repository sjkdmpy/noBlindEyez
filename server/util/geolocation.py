from geopy.adapters import AioHTTPAdapter
from geopy.geocoders import Nominatim


async def address2coords(address: str) -> dict[float, float]:
	async with Nominatim(
		user_agent="NoBlindEyez",
		adapter_factory=AioHTTPAdapter,
	) as geolocator:
		location = await geolocator.geocode(address)
		if location:
			return {
				"latitude": location.latitude,
				"longitude": location.longitude
			}
		else:
			return None