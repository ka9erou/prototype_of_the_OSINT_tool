# modules/phone_search.py

import asyncio
import aiohttp
# from config import DEHASHED_EMAIL, DEHASHED_API_KEY


async def find_phones(username, social_profiles=None, emails=None):
    phones = []

    # from social
    if social_profiles:
        for net, profile in social_profiles.items():
            if isinstance(profile, dict) and 'phone' in profile and profile['phone']:
                phones.append(profile['phone'])
    
    # from breaches
    # if emails:
    #     for email in emails:
    #         try:
    #             async with aiohttp.ClientSession() as session:
    #                 auth = aiohttp.BasicAuth(DEHASHED_EMAIL, DEHASHED_API_KEY)
    #                 params = {'query': email}
    #                 async with session.get('https://api.dehashed.com/search', params=params, auth=auth) as response:
    #                     if response.status == 200:
    #                         data = await response.json()
    #                         for entry in data.get('entries', []):
    #                             if 'phone' in entry and entry['phone']:
    #                                 phones.append(entry['phone'])
    #         except Exception as e:
    #             pass
    
    return list(set(phones))