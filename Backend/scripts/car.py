import requests
import json

# 🔥 Load API Key
GEOPIFY_API_KEY = ""  # Add your Geoapify API Key

# ✅ Constants
FUEL_PRICE_PER_LITER = 100  # INR
FUEL_EFFICIENCY = 15  # km per liter

# ✅ Cache for Geocoding to Avoid Repeated API Calls
geo_cache = {}

# ✅ Function to get lat/lon using Geopify Geocoding API
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
    
    print(f"❌ Error fetching geocode for {city_name}")
    return None, None

# ✅ Function to get route details from Geoapify
def get_travel_details(start_lat, start_lon, dest_lat, dest_lon):
    url = f"https://api.geoapify.com/v1/routing?waypoints={start_lat},{start_lon}|{dest_lat},{dest_lon}&mode=drive&apiKey={GEOPIFY_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "features" in data and len(data["features"]) > 0:
            route_info = data["features"][0]["properties"]
            return route_info["distance"] / 1000, route_info["time"] / 60  # km, mins
    
    print(f"❌ Error fetching route: {response.status_code}")
    return None, None

# ✅ Function to calculate fuel cost
def calculate_fuel_cost(distance_km):
    fuel_needed = distance_km / FUEL_EFFICIENCY
    return round(fuel_needed * FUEL_PRICE_PER_LITER, 2), round(fuel_needed, 2)  # Cost & Liters

# ✅ Function to generate travel itinerary with OSM Link
def generate_itinerary_car(origin_city, destination_city):
    results = {}

    # 🔹 Step 1: Geocode Cities
    origin_lat, origin_lon = geocode_city(origin_city)
    dest_lat, dest_lon = geocode_city(destination_city)

    if not origin_lat or not dest_lat:
        return {"error": "Failed to get coordinates for given locations"}

    # 🔹 Step 2: Get Route Info
    car_distance, car_time = get_travel_details(origin_lat, origin_lon, dest_lat, dest_lon)

    # 🔹 Step 3: Generate Itinerary
    if car_distance and car_time:
        fuel_cost, fuel_liters = calculate_fuel_cost(car_distance)
        results = {
            "Total Distance (km)": round(car_distance, 2),
            "Total Time": f"{int(car_time // 60)} hrs {int(car_time % 60)} mins",
            "Estimated Fuel Cost (INR)": fuel_cost,
            "Fuel Required (Liters)": fuel_liters,
            "Route Map (OSM)": f"https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&route={origin_lat},{origin_lon};{dest_lat},{dest_lon}"
        }

    return results
