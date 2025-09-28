# modules/username_search.py

import asyncio
from .social_media import search_social_media
from .email_search import find_emails
from .phone_search import find_phones
from .geolocation import geolocate_phone
from .map_generator import generate_map
from config import REQUEST_DELAY


async def username_investigation(username):
    results = {}
    
    # Поиск в социальных сетях
    print("Searching social media profiles...")
    social_results = await search_social_media(username)
    results['social_media'] = social_results
    
    # Проверяем, есть ли хоть какие-то данные в социальных сетях
    has_valid_social_data = any(
        isinstance(profile, dict) and 'error' not in profile 
        for profile in social_results.values()
    )
    
    if not has_valid_social_data:
        print("Warning: No valid social media data found")
        # Если нет данных из соцсетей, все равно продолжаем поиск email и телефонов
        # но используем только username для поиска
        email_source = {'username': username}
        phone_source = {'username': username}
    else:
        email_source = results['social_media']
        phone_source = results['social_media']
    
    # Поиск email-адресов
    print("Searching for email addresses...")
    results['emails'] = await find_emails(username, email_source)
    
    # Поиск телефонных номеров
    print("Searching for phone numbers...")
    results['phones'] = await find_phones(username, phone_source, results['emails'])
    
    # Геолокация и карты
    print("Performing geolocation...")
    results['geolocations'] = []
    if results['phones']:
        for phone in results['phones']:
            location_data = await geolocate_phone(phone)
            if location_data and 'coordinates' in location_data:
                map_url = generate_map(location_data['coordinates'])
                location_data['map_url'] = map_url
            results['geolocations'].append({phone: location_data})
            
            await asyncio.sleep(REQUEST_DELAY)
    else:
        print("No phone numbers found for geolocation")
    
    return results