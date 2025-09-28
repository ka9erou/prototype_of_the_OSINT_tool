# modules/data_breaches.py

# import asyncio
# import aiohttp
# import pyhibp
# from config import DEHASHED_EMAIL, DEHASHED_API_KEY, HIBP_API_KEY


# pyhibp.set_api_key(key=HIBP_API_KEY)
# pyhibp.set_user_agent(ua='OSINT-Tool/1.0')


# async def check_dehashed(query):
#     results = []
#     try:
#         async with aiohttp.ClientSession() as session:
#             auth = aiohttp.BasicAuth(DEHASHED_EMAIL, DEHASHED_API_KEY)
#             params = {'query': query}
#             async with session.get('https://api.dehashed.com/search', params=params, auth=auth) as response:
#                 if response.status == 200:
#                     data = await response.json()
#                     results = data.get('entries', [])
#     except Exception as e:
#         return {'error': str(e)}
#     
#     return results


# async def check_hibp_email(email):
#     try:
#         breaches = await asyncio.to_thread(pyhibp.get_account_breaches, account=email)
#         return breaches
#     except Exception as e:
#         return {'error': str(e)}
    

# async def check_data_breaches(username, emails, phones):
#     results = {'dehashed': {}, 'hibp': {}}
#
#     # DeHashed for username, emails, phones
#     results['dehashed']['username'] = await check_dehashed(username)
#     for email in emails:
#         results['dehashed'][f'email_{email}'] = await check_dehashed(email)
#         results['hibp'][email] = await check_hibp_email(email)
#     for phone in phones:
#         results['dehashed'][f'phone_{phone}'] = await check_dehashed(phone)
#
#     return results