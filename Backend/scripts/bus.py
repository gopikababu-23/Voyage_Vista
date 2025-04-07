import requests
import json
import time

# 🔥 Load API Key
GEOPIFY_API_KEY = ""  # Add your Geoapify API Key

# ✅ Constants
BUS_CLASS_MULTIPLIERS = {"sleeper": 1.8, "semi-sleeper": 1.5, "luxury": 2.0}
BUS_FARES = {"local": 12.5, "intercity": 300, "long_distance": 1000}

# ✅ Cache for Geocoding to Avoid Repeated API Calls
geo_cache = {}

# ✅ Function to convert city name to lat/lon (Geocoding)
def geocode_city(city_name):
    if city_name in geo_cache:
        return geo_cache[city_name]  # Return cached result

    url = f"https://api.geoapify.com/v1/geocode/search?text={city_name}&format=json&apiKey={GEOPIFY_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            lat, lon = data["results"][0]["lat"], data["results"][0]["lon"]
            geo_cache[city_name] = (lat, lon)  # Store in cache
            return lat, lon
    
    print(f"❌ Geocoding Failed for {city_name}")
    return None, None

# ✅ Function to get route details from Geoapify
def get_travel_details(start_lat, start_lon, dest_lat, dest_lon):
    url = f"https://api.geoapify.com/v1/routing?waypoints={start_lat},{start_lon}|{dest_lat},{dest_lon}&mode=bus&apiKey={GEOPIFY_API_KEY}"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "features" in data and len(data["features"]) > 0:
            route_info = data["features"][0]["properties"]
            return route_info["distance"] / 1000, route_info["time"] / 60  # km, mins
    
    print(f"❌ Error fetching route: {response.status_code} - {response.text}")
    return None, None

# ✅ Function to calculate bus fare
def calculate_bus_fare(distance_km, bus_class, num_members):
    if distance_km <= 50:
        fare = BUS_FARES["local"]
    elif distance_km <= 200:
        fare = BUS_FARES["intercity"]
    else:
        fare = BUS_FARES["long_distance"]

    return round(float(fare) * BUS_CLASS_MULTIPLIERS.get(bus_class.lower(), 1) * int(num_members or 1), 2)

# ✅ Convert minutes to hours + minutes
def format_time(minutes):
    return f"{int(minutes // 60)} hrs {int(minutes % 60)} mins"

# ✅ Function to generate travel itinerary
def generate_itinerary_bus(origin_city, destination_city, bus_class, num_members):
    results = {}

    start_time = time.time()

    # 🔹 Step 1: Geocode Cities
    origin_lat, origin_lon = geocode_city(origin_city)
    dest_lat, dest_lon = geocode_city(destination_city)

    if not origin_lat or not dest_lat:
        return {"error": "Geocoding failed for one or both locations."}

    # 🔹 Step 2: Get Route Info
    bus_distance, bus_time = get_travel_details(origin_lat, origin_lon, dest_lat, dest_lon)

    # 🔹 Step 3: Generate Itinerary
    if bus_distance and bus_time:
        results = {
            "Total Distance (km)": round(bus_distance, 2),
            "Total Time": format_time(bus_time),
            "Average Bus Fare (INR)": calculate_bus_fare(bus_distance, bus_class, num_members),
            "Booking Link": "https://www.redbus.in/",
        }

    return results
