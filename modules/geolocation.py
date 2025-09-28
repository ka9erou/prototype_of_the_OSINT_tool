# modules/geolocation.py


import asyncio
import aiohttp
# from config import IPAPI_KEY, OPENCAGE_API_KEY
from config import OPENCAGE_API_KEY


async def geolocate_phone(phone_number):
    location_data = {}
    # try:
    #     async with aiohttp.ClientSession() as session:
    #         url = "http://apilayer.net/api/validate"
    #         params = {
    #             'access_key': IPAPI_KEY,
    #             'number': phone_number,
    #             'country_code': '',
    #             'format': 1
    #         }
    #         async with session.get(url, params=params) as response:
    #             data = await response.json()
    #             
    #             if data.get('valid'):
    #                 location_data = {
    #                     'country': data.get('country_name'),
    #                     'location': data.get('location'),  # e.g., city or region
    #                     'carrier': data.get('carrier'),
    #                     'line_type': data.get('line_type'),
    #                 }
    # except Exception as e:
    #     return {'error': str(e)}
    
    # Geocode location string to coordinates using OpenCage
    # if 'location' in location_data and location_data['location']:
    #     try:
    #         async with aiohttp.ClientSession() as session:
    #             url = "https://api.opencagedata.com/geocode/v1/json"
    #             params = {
    #                 'q': location_data['location'] + ', ' + location_data['country'],
    #                 'key': OPENCAGE_API_KEY
    #             }
    #             async with session.get(url, params=params) as response:
    #                 data = await response.json()
    #                 if data['results']:
    #                     geom = data['results'][0]['geometry']
    #                     location_data['coordinates'] = (geom['lat'], geom['lng'])
    #     except Exception as e:
    #         location_data['geocode_error'] = str(e)
    
    return location_data