import requests
import json
from datetime import datetime
from flask import jsonify

# 🔥 Geopify & Amadeus API Keys (Replace with your keys)
GEOPIFY_API_KEY = ""
AMADEUS_API_KEY = ""
AMADEUS_API_SECRET = ""

# ✅ Function to Get Latitude & Longitude from Geopify
def get_lat_lon_geopify(city_name):
    url = f"https://api.geoapify.com/v1/geocode/search?text={city_name}&apiKey={GEOPIFY_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json().get("features", [])
        if data:
            coordinates = data[0]["geometry"]["coordinates"]
            return coordinates[1], coordinates[0]  # (Latitude, Longitude)
    return None, None

# ✅ Function to Get Amadeus Access Token
def get_amadeus_access_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_API_KEY,
        "client_secret": AMADEUS_API_SECRET
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token") if response.status_code == 200 else None

# ✅ Function to Search Hotels by Latitude & Longitude
def search_hotels(lat, lon, radius_km, rating, access_token):
    url = f"https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-geocode?latitude={lat}&longitude={lon}&radius={radius_km}&radiusUnit=KM&ratings={rating}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("data", [])
    return None

# ✅ Function to Calculate Price Per Night
def calculate_price_per_night(budget_min, budget_max, number_of_days, rating):
    tax_rates = {1: 0.1, 2: 0.12, 3: 0.14, 4: 0.16, 5: 0.18}
    tax = int(budget_min) * tax_rates.get(int(rating), 0)
    return (int(budget_min) + tax) / number_of_days

# ✅ Function to Calculate Number of Days
def calculate_number_of_days(start_date, end_date):
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    return max((end_date_obj - start_date_obj).days, 1)

# ✅ Function to Get the Best Hotel Based on Budget
def get_best_hotel(city_name, radius_km, rating, budget_min, budget_max, start_date, end_date):
    lat, lon = get_lat_lon_geopify(city_name)
    if lat is None or lon is None:
        return {"error": f"Unable to find coordinates for '{city_name}'."}
    
    access_token = get_amadeus_access_token()
    if not access_token:
        return {"error": "Failed to get Amadeus API token."}
    
    hotels = search_hotels(lat, lon, radius_km, rating, access_token)
    if not hotels:
        return {"error": "No hotels found or Amadeus API issue."}
    
    number_of_days = calculate_number_of_days(start_date, end_date)
    estimated_price_per_night = calculate_price_per_night(budget_min, budget_max, number_of_days, rating)
    
    hotels_sorted_by_distance = sorted(hotels, key=lambda x: x.get("distance", {}).get("value", float("inf")))
    
    for hotel in hotels_sorted_by_distance:
        return {
            "name": hotel.get("name", "Unknown"),
            "distance_km": hotel.get("distance", {}).get("value", "N/A"),
            "latitude": hotel.get("geoCode", {}).get("latitude", "N/A"),
            "longitude": hotel.get("geoCode", {}).get("longitude", "N/A"),
            "rating": hotel.get("rating", "N/A"),
            "price_per_night": round(estimated_price_per_night, 2),
            "total_cost": round(estimated_price_per_night * number_of_days, 2),
            "booking_link": f"https://www.booking.com/hotel/{hotel.get('hotelId', '')}"
        }
    
    return {"error": "No hotels within budget found."}
