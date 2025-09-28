# modules/email_search.py

import asyncio
# from spiderfoot import SpiderFoot, SpiderFootTarget


async def find_emails(username, social_profiles=None):
    emails = []
    # try:
    #     sf = SpiderFoot({'default': {}})    # config
    #     target = SpiderFootTarget(username, 'USERNAME')
    #     scan = sf.scan(target, 'ALL')   # all modules
    #     results = scan.getResults()
    #     for res in results:
    #         if res['type'] == 'EMAILADDR':
    #             emails.append(res['data'])
    #
    # except Exception as e:
    #     print(f'Spiderfoot error: {str(e)}')

    if social_profiles:
        for net, profile in social_profiles.items():
            if isinstance(profile, dict) and 'email' in profile:
                emails.append(profile['email'])

    return list(set(emails))