import requests
import argparse
import json

# 🔥 Load API Key
GEOPIFY_API_KEY = ""  # Add your API key here

# ✅ Constants
FUEL_PRICE_PER_LITER = 100  # INR
FUEL_EFFICIENCY = 15  # km per liter

# ✅ Function to get lat/lon using Geopify Geocoding API
def geocode_city(city_name):
    url = f"https://api.geoapify.com/v1/geocode/search?text={city_name}&format=json&apiKey={GEOPIFY_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            return data["results"][0]["lat"], data["results"][0]["lon"]
    print(f"❌ Error fetching geocode for {city_name}")
    return None, None

# ✅ Function to get route details from Geoapify
def get_travel_details(start, destination, mode):
    url = f"https://api.geoapify.com/v1/routing?waypoints={start}|{destination}&mode={mode}&apiKey={GEOPIFY_API_KEY}"
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
def generate_itinerary_rental(origin_city, destination_city):
    results = {}

    # Convert city names to lat/lon
    origin_lat, origin_lon = geocode_city(origin_city)
    destination_lat, destination_lon = geocode_city(destination_city)

    if not origin_lat or not destination_lat:
        return {"error": "Failed to get coordinates for given locations"}

    start_location = f"{origin_lat},{origin_lon}"
    destination_location = f"{destination_lat},{destination_lon}"

    # Car Travel Details
    car_distance, car_time = get_travel_details(start_location, destination_location, "drive")
    if car_distance and car_time:
        fuel_cost, fuel_liters = calculate_fuel_cost(car_distance)
        results["Rental"] = {
            "Total Distance (km)": round(car_distance, 2),
            "Total Time": f"{int(car_time // 60)} hrs {int(car_time % 60)} mins",
            "Estimated Fuel Cost (INR)": fuel_cost,
            "Fuel Required (Liters)": fuel_liters,
            "Rental cost per day": "3000 INR",
            "Car Rental Service": "https://www.zoomcar.com/",
            "Route Map (OSM)": f"https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&route={origin_lat},{origin_lon};{destination_lat},{destination_lon}"
        }

    return results

# ✅ Command-line argument handling
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--origin", required=True, help="Origin city name")
    parser.add_argument("--destination", required=True, help="Destination city name")
    args = parser.parse_args()

    itinerary = generate_itinerary_rental(args.origin, args.destination)
    print(json.dumps(itinerary, indent=2))
