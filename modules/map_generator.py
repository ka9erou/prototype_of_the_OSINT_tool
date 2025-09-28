# modules/map_generator.py

def generate_map(coordinates):
    if not coordinates:
        return None
    lat, lon = coordinates
    return f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"