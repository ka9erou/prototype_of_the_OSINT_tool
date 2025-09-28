# modules/social_media.py

import asyncio
import aiohttp
from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ClientError
from config import (
    TELEGRAM_API_ID, TELEGRAM_API_HASH,
    VK_ACCESS_TOKEN, INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD,
    REQUEST_DELAY, TIMEOUT, MAX_RETRIES
)

async def search_tg(username):
    try:
        async with TelegramClient('session', TELEGRAM_API_ID, TELEGRAM_API_HASH) as client:
            user = await client.get_entity(username)
            
            # Получаем полную информацию о пользователе
            full_user = await client(GetFullUserRequest(user))
            
            return {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'bio': full_user.about if hasattr(full_user, 'about') else None,
                'phone': user.phone if hasattr(user, 'phone') else None,
                'profile_url': f'https://t.me/{username}'
            }
        
    except Exception as e:
        return {'error': str(e)}

async def search_vk(username):
    for attempt in range(MAX_RETRIES):
        try:
            async with aiohttp.ClientSession() as session:
                url = "https://api.vk.com/method/users.get"
                params = {
                    'user_ids': username,
                    'fields': 'photo_200,contacts,city,country,about',
                    'access_token': VK_ACCESS_TOKEN,
                    'v': '5.131'
                }

                async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=TIMEOUT)) as response:
                    data = await response.json()
                    
                    if 'error' in data:
                        return {'error': f"VK API error: {data['error']['error_msg']}"}
                    
                    if 'response' in data and data['response']:
                        user = data['response'][0]
                        
                        # Проверяем, не заблокирован ли профиль
                        if 'deactivated' in user:
                            return {'error': f"Profile deactivated: {user['deactivated']}"}

                        return {
                            'id': user['id'],
                            'first_name': user.get('first_name'),
                            'last_name': user.get('last_name'),
                            'profile_url': f'https://vk.com/id{user["id"]}',
                            'photo': user.get('photo_200'),
                            'phone': user.get('mobile_phone'),
                            'city': user.get('city', {}).get('title') if 'city' in user else None,
                            'country': user.get('country', {}).get('title') if 'country' in user else None,
                            'bio': user.get('about')
                        }
                    else:
                        return {'error': 'VK profile not found'}
        except asyncio.TimeoutError:
            if attempt < MAX_RETRIES - 1:
                print(f"VK timeout, retrying... (attempt {attempt + 1}/{MAX_RETRIES})")
                await asyncio.sleep(2)
                continue
            return {'error': 'VK API request timeout after multiple attempts'}
        except Exception as e:
            return {'error': str(e)}

async def search_inst(username):
    """Поиск в Instagram с использованием instagrapi"""
    for attempt in range(MAX_RETRIES):
        try:
            print(f"Instagram attempt {attempt + 1}/{MAX_RETRIES} for username: {username}")
            cl = Client()
            
            # Настройка тайм-аута для запросов
            cl.request_timeout = TIMEOUT
            
            # Аутентификация с использованием логина и пароля
            try:
                cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
                print(f"Successfully logged in to Instagram as {INSTAGRAM_USERNAME}")
            except Exception as e:
                print(f"Instagram login error: {str(e)}")
                return {'error': f'Instagram login error: {str(e)}'}
            
            # Получение информации о пользователе
            user_id = cl.user_id_from_username(username)
            user_info = cl.user_info(user_id)
            
            print(f"Successfully retrieved Instagram profile for {username}")
            return {
                'username': user_info.username,
                'full_name': user_info.full_name,
                'bio': user_info.biography,
                'profile_url': f'https://instagram.com/{username}',
                'followers': user_info.follower_count,
                'following': user_info.following_count,
                'posts': user_info.media_count,
                'is_private': user_info.is_private,
                'is_verified': user_info.is_verified
            }
        
        except (LoginRequired, ClientError) as e:
            print(f"Instagram login error: {str(e)}")
            if attempt < MAX_RETRIES - 1:
                print(f"Retrying... (attempt {attempt + 1}/{MAX_RETRIES})")
                await asyncio.sleep(2)
                continue
            return {'error': f'Instagram login error: {str(e)}'}
        except Exception as e:
            print(f"Instagram error: {str(e)}")
            if attempt < MAX_RETRIES - 1:
                print(f"Retrying... (attempt {attempt + 1}/{MAX_RETRIES})")
                await asyncio.sleep(2)
                continue
            return {'error': f'Instagram error: {str(e)}'}

async def search_social_media(username):
    results = {}

    tasks = [
        search_tg(username),
        search_vk(username),
        search_inst(username),
    ]

    social_results = await asyncio.gather(*tasks, return_exceptions=True)

    # Исправляем присваивание результатов
    results['telegram'] = social_results[0] if not isinstance(social_results[0], Exception) else {'error': str(social_results[0])}
    results['vk'] = social_results[1] if not isinstance(social_results[1], Exception) else {'error': str(social_results[1])}
    results['instagram'] = social_results[2] if not isinstance(social_results[2], Exception) else {'error': str(social_results[2])}

    await asyncio.sleep(REQUEST_DELAY)
    return results