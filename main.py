# main.py

import argparse
import asyncio
import json
from datetime import datetime
from modules.username_search import username_investigation
from modules.reverse_image import reverse_image_search
from modules.image_upload import upload_local_image
from utils.export_utils import save_report

# Debug: Print Python path
import sys

async def main():
    print("Inside main function...")
    parser = argparse.ArgumentParser(description='OSINT Investigation Tool')
    parser.add_argument('--username', help='Username to investigate')
    parser.add_argument('--image', help='Image URL for reverse search')
    parser.add_argument('--local_image', help='Local image path for reverse search')
    parser.add_argument('--output', default='report', help='Output file name')

    args = parser.parse_args()
    print(f"Arguments received: {args}")

    if not args.username and not args.image and not args.local_image:
        print("Please provide either --username, --image or --local_image argument")
        return
    
    results = {}
    print("Results dictionary initialized...")

    image_url = None
    if args.image:
        image_url = args.image
        print(f"Using image URL: {image_url}")
    elif args.local_image:
        print(f"Uploading local image: {args.local_image}")
        image_url = await upload_local_image(args.local_image)
        if not image_url:
            print("Failed to upload local image. Aborting.")
            return
        print(f"Uploaded image URL: {image_url}")
        
    if args.username:
        print(f"Starting investigation for username: {args.username}")
        results = await username_investigation(args.username)
        
        # Выводим результаты в консоль для удобства
        print("\n=== Investigation Results ===")
        for platform, data in results['social_media'].items():
            print(f"\n{platform.capitalize()} Profile:")
            if 'error' in data:
                print(f"  Error: {data['error']}")
            else:
                for key, value in data.items():
                    print(f"  {key}: {value}")
        
        if results['emails']:
            print("\nEmails:")
            for email in results['emails']:
                print(f"  {email}")
        
        if results['phones']:
            print("\nPhones:")
            for phone in results['phones']:
                print(f"  {phone}")
        
        if results['geolocations']:
            print("\nGeolocations:")
            for geo in results['geolocations']:
                for phone, data in geo.items():
                    print(f"  Phone: {phone}")
                    print(f"    {data}")
    
    elif image_url:
        print(f"Starting reverse image search for: {image_url}")
        image_results = await reverse_image_search(image_url)
        print(f"Image search results: {image_results}")

        results['image_search'] = image_results

        for profile in image_results.get('profiles', []):
            if 'username' in profile:
                username = profile['username']
                if username:
                    print(f"Investigating found profile: {username}")
                    profile_results = await username_investigation(username)
                    results[username] = profile_results

                    # Выводим результаты для каждого найденного профиля
                    print(f"\n=== Results for {username} ===")
                    for platform, data in profile_results['social_media'].items():
                        print(f"\n{platform.capitalize()} Profile:")
                        if 'error' in data:
                            print(f"  Error: {data['error']}")
                        else:
                            for key, value in data.items():
                                print(f"  {key}: {value}")

    # Saving report
    report_filename = f"outputs/reports/{args.output}_{datetime.now().strftime('%Y-%m-%d__%H-%M-%S')}.json"
    print(f"Saving report to: {report_filename}")
    save_report(results, report_filename)

    print(f"Investigation complete. Report saved to {report_filename}")

if __name__ == '__main__':
    print("Running asyncio.run(main())...")
    asyncio.run(main())