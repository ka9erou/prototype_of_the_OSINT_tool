# modules/image_upload.py

import aiohttp
from config import IMGBB_API_KEY

async def upload_local_image(file_path):
    try:
        async with aiohttp.ClientSession() as session:
            with open(file_path, 'rb') as f:
                data = aiohttp.FormData()
                data.add_field('image', f)
                async with session.post('https://api.imgbb.com/1/upload', params={'key': IMGBB_API_KEY}, data=data) as response:
                    if response.status == 200:
                        json_data = await response.json()
                        return json_data['data']['url']
                    else:
                        raise Exception(f"Upload failed with status {response.status}")
    except Exception as e:
        print(f'Image upload error: {str(e)}')
        return None       