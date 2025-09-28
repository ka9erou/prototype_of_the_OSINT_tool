# modules/reverse_image.py

import asyncio
import aiohttp
# from config import GOOGLE_API_KEY, GOOGLE_CSE_ID


# async def google_reverse_image_search(image_url):
#     try:
#         async with aiohttp.ClientSession() as session:
#             search_url = "https://www.googleapis.com/customsearch/v1"
#             params = {
#                 'key': GOOGLE_API_KEY,
#                 'cx': GOOGLE_CSE_ID,
#                 'searchType': 'image',
#                 'imgUrl': image_url
#             }
#
#             async with session.get(search_url, params=params) as response:
#                 data = await response.json()
#
#                 profiles = []
#                 for item in data.get('items', []):
#                     link = item.get('link', '')
#                     if any(domain in link for domain in ['vk.com', 't.me', 'instagram.com', 'facebook.com', 'twitter.com']):
#                         profiles.append({
#                             'url': link,
#                             'title': item.get('title'),
#                             'image': item.get('image', {}).get('thumbnailLink'),
#                             'username': link.split('/')[-1] if '/' in link else None
#                         })
#
#                 return {'profiles': profiles}
#     except Exception as e:
#         return {'error': str(e)}


async def reverse_image_search(image_url):
    results = {}

    tasks = [
        # google_reverse_image_search(image_url)
    ]

    search_results = await asyncio.gather(*tasks, return_exceptions=True)

    # results['google'] = search_results[0]
    results['google'] = {'error': 'Google API keys not configured'}

    all_profiles = []
    # for service_result in search_results:
    #     if not isinstance(service_result, Exception) and 'profiles' in service_result:
    #         all_profiles.extend(service_result['profiles'])

    results['profiles'] = all_profiles

    return results