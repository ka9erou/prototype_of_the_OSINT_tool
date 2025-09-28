# prototype_of_the_OSINT_tool

OSINT Investigation Tool

A comprehensive Open Source Intelligence (OSINT) tool for gathering information from social media platforms and other online sources. This tool helps investigators, security researchers, and authorized personnel collect publicly available information about individuals across multiple platforms.

🚀 Current Features

✅ Implemented Social Media Platforms
- Telegram - Full profile information including bio, phone number, and user details
- Instagram - Profile data, follower counts, verification status, and biography
- VKontakte (VK) - User information, contact details, location data, and profile photos

🔍 Search Capabilities
- **Username-based investigation** across multiple platforms simultaneously
- **Reverse image search** to find profiles using photos
- **Local image upload** for reverse search analysis
- **Email address discovery** from social media profiles
- **Phone number extraction** from linked accounts
- **Geolocation data** from phone numbers with map generation

📋 Planned Features (Under Development)

🔄 Social Media Platforms
- Twitter/X - Profile information and activity
- Facebook - Basic profile data and public information

🔧 Additional Modules
- **SpiderFoot integration** for comprehensive email discovery
- **Data breach checking** via Dehashed and HIBP APIs
- **Advanced phone number validation** and carrier information
- **Comprehensive geolocation services**


Configure API keys
   - Copy `config.py` and update with your API credentials

🎯 Usage

Command Line Interface

1. Username Investigation
python main.py --username target_username

Example:
python main.py --username john_doe

2. Reverse Image Search
# Using image URL
python main.py --image https://example.com/profile.jpg

# Using local image file
python main.py --local_image /path/to/local/image.jpg


#### 3. Combined Search
python main.py --username target_user --local_image photo.jpg --output comprehensive_report


📊 Output

The tool generates comprehensive JSON reports containing:

Social Media Data
- Profile information (name, bio, verification status)
- Contact details (phone numbers, emails)
- Statistical data (followers, posts count)
- Profile URLs and identifiers

Investigation Results
- Social Media Profiles: Telegram, Instagram, VK data
- Contact Information: Discovered emails and phone numbers
- Geolocation Data: Coordinates and map links
- Image Search Results: Found profiles from reverse image search


Report Structure
outputs/reports/
├── report_2024-01-15__14-30-25.json
└── ...


## 🔧 Technical Details

Architecture
- Asynchronous Processing: Concurrent API requests for faster results
- Modular Design: Separate modules for each platform and functionality
- Error Handling: Robust error handling with retry mechanisms
- Rate Limiting: Configurable delays between requests

Dependencies
- `aiohttp` - Asynchronous HTTP requests
- `telethon` - Telegram API client
- `instagrapi` - Instagram API wrapper
- `python-opencage` - Geocoding services


⚠️ Important Notes

Legal and Ethical Usage
- This tool is intended for **authorized investigations only**
- Ensure compliance with local laws and platform Terms of Service
- Respect privacy and data protection regulations
- Use only for legitimate security research or authorized penetration testing

Limitations
- API Rate Limits: Respect platform API limitations
- Account Requirements: Some services require valid accounts
- Geographical Restrictions: Some APIs may have regional limitations
- Platform Changes: Social media APIs frequently change

🚧 Development Status

Current Implementation
- ✅ Core social media platforms (Telegram, Instagram, VK)
- ✅ Basic reverse image search infrastructure (prototype)
- ✅ Email and phone extraction from profiles
- ✅ Geolocation and mapping (prototype)
- ✅ Report generation

Planned Enhancements
- 🔄 Twitter/X integration
- 🔄 Facebook profile search
- 🔄 SpiderFoot integration for OSINT correlation
- 🔄 Data breach checking (Dehashed, HIBP)
- 🔄 Advanced image analysis
- 🔄 Web interface
- 🔄 Database storage for results


🆘 Troubleshooting

Common Issues

1. Instagram Login Errors
   - Ensure 2FA is disabled or handle appropriately
   - Check account credentials in config
   - Verify account is not temporarily blocked

2. Telegram API Issues
   - Verify API credentials from my.telegram.org
   - Check if the target username exists

3. VK API Limitations
   - Ensure valid access token with proper permissions
   - Check token expiration

4. Rate Limiting
   - Adjust `REQUEST_DELAY` in config for aggressive scanning
   - Monitor API usage limits

🤝 Contributing

This project is under active development. Contributions are welcome for:
- Additional social media platforms
- Improved error handling
- Enhanced reporting features
- Documentation improvements

📄 License

This project is intended for educational and authorized security research purposes only. Users are responsible for complying with all applicable laws and regulations.

---

Disclaimer: This tool should only be used for legitimate security research or with explicit permission from the investigated parties. Misuse of this tool may violate laws and platform terms of service.
