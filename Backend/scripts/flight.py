import requests
import json
from flask import Flask, request, jsonify

# 🔥 Add your Amadeus API credentials
API_KEY = ""  # Add your Amadeus API Key
API_SECRET = ""  # Add your Amadeus API Secret

app = Flask(__name__)

# ✅ Get Access Token
def get_amadeus_access_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token", None) if response.status_code == 200 else None

# ✅ Convert City Name to IATA Code
def get_iata_code(city_name, access_token):
    # Manually defined IATA codes for major cities
    manual_iata_codes = {
        "Malaysia": "KUL",
        "Penang": "PEN",
        "Los Angeles": "LAX",
        "San Francisco": "SFO",
        "Chicago": "ORD",
        "Miami": "MIA",
        "Washington dc": "IAD",
        "Vancouver": "YVR",
        "Montreal": "YUL",
        "Manchester": "MAN",
        "Paris": "CDG",
        "Rome": "FCO",
        "Venice": "VCE",
        "Milan": "MXP",
        "Barcelona": "BCN",
        "Madrid": "MAD",
        "Zurich": "ZRH",
        "Geneva": "GVA",
        "Vienna": "VIE",
        "Athens": "ATH",
        "Santorini": "JTR",
        "Istanbul": "IST",
        "Amsterdam": "AMS",
        "Dublin": "DUB",
        "Berlin": "BER",
        "Frankfurt": "FRA",
        "Munich": "MUC",
        "Netherland": "AMS",
        "Ireland": "DUB",
        "Riyadh": "RUH",
        "Jeddah": "JED",
        "Doha": "DOH",
        "Cairo": "CAI",
        "Luxor": "LXR",
        "Nairobi": "NBO",
        "Marrakech": "RAK",
        "Tel Aviv": "TLV",
        "Sydney": "SYD",
        "Melbourne": "MEL",
        "Brisbane": "BNE",
        "Australia": "PER",
        "Auckland": "AKL",
        "Wellington": "WLG",
        "Newzealand":"AKL",
        "Osaka": "KIX",
        "Japan": "HND",
        "Beijing": "PEK",
        "Shanghai": "PVG",
        "Hong Kong": "HKG",
        "China": "HKG",
        "Singapore": "SIN",
        "Dubai": "DXB",
        "Abu Dhabi": "AUH",
        "Seoul": "ICN",
        "Hanoi": "HAN",
        "Manila": "MNL",
        "Kuala Lumpur": "KUL",
        "Bali": "DPS",
        "Taipei": "TPE",
        "Maldives": "MLE",
        "Indonesia": "DPS",
        "Melbourne": "MEL",
        "Jakarta": "CGK",
        "Bangkok": "BKK",
        "Thailand": "BKK",
        "Toronto": "YYZ",
        "Canada": "YYZ",
        "Vancouver": "YVR",
        "Johannesburg": "JNB",
        "Cape Town": "CPT",
        "South Africa": "CPT",
        "Bangalore": "BLR",
        "Kolkata": "CCU",
        "Hyderabad": "HYD",
        "Dubai": "DXB",
        "New York": "JFK",
        "Los Angeles": "LAX",
        "London": "LHR",
        "Tokyo": "HND",
        "Hawaii": "HNL",
        "Honolulu": "HNL",
        "Sydney": "SYD",
        "Port Blair": "IXZ",
        "Andaman and Nicobar Islands":"IXZ",
        "Colombo": "CMB",
        "Sri Lanka": "CMB",
        "Brazil":"GRU",
        "Argentina":"EZE",
        "Nepal":"KTM",
        "Kuwait":"KWI",
        "Muscat":"MCT",
        "Oman":"MCT",
        "Portugal":"LIS",
        "Hungary":"BUD",
        "Mexico":"MEX"
    }

    # Check if city is in the manual mapping
    if city_name in manual_iata_codes:
        return manual_iata_codes[city_name]

    # Otherwise, fetch from Amadeus API
    url = "https://test.api.amadeus.com/v1/reference-data/locations"
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    params = {"keyword": city_name, "subType": "CITY"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data", [])
        if data:
            return data[0]["iataCode"]  # Return first matching IATA code
        else:
            print(f"⚠️ No IATA code found for {city_name}. Using manual mapping if available.")
            return manual_iata_codes.get(city_name, city_name)  # Fallback to manual mapping or city name
    else:
        print(f"❌ Error fetching IATA code for {city_name}: {response.json()}")
        return manual_iata_codes.get(city_name, city_name)  # Fallback to manual mapping or city name
    
# ✅ Extract relevant flight details
def extract_flight_details(response_data):
    if "data" not in response_data:
        return {"error": "No flight data available"}

    flights = response_data["data"]
    if not flights:
        return {"error": "No flight offers found"}

    # Pick the first available flight offer
    flight_offer = flights[0]

    onward_flight = {}
    return_flight = {}

    try:
        itineraries = flight_offer["itineraries"]
        
        # Extract onward flight details
        if len(itineraries) > 0:
            onward_segment = itineraries[0]["segments"][0]
            onward_flight = {
                "airline": onward_segment["carrierCode"],
                "flight_number": onward_segment["number"],
                "departure_airport": onward_segment["departure"]["iataCode"],
                "departure_time": onward_segment["departure"]["at"],
                "arrival_airport": onward_segment["arrival"]["iataCode"],
                "arrival_time": onward_segment["arrival"]["at"],
                "duration": itineraries[0]["duration"],
                "price": flight_offer["price"]["total"]
            }

        # Extract return flight details if available
        if len(itineraries) > 1:
            return_segment = itineraries[1]["segments"][0]
            return_flight = {
                "airline": return_segment["carrierCode"],
                "flight_number": return_segment["number"],
                "departure_airport": return_segment["departure"]["iataCode"],
                "departure_time": return_segment["departure"]["at"],
                "arrival_airport": return_segment["arrival"]["iataCode"],
                "arrival_time": return_segment["arrival"]["at"],
                "duration": itineraries[1]["duration"],
                "price": flight_offer["price"]["total"]
            }

    except KeyError as e:
        print(f"❌ Error extracting flight details: Missing key {str(e)}")
        return {"error": "Invalid response structure from Amadeus API"}

    return {"onward_flight": onward_flight, "return_flight": return_flight}

# ✅ Get Flight Offers
def get_flights(origin_city, destination_city, departure_date, return_date, adults, children,infant, max_price, travel_class, currency_code):
    access_token = get_amadeus_access_token()
    if not access_token:
        return {"error": "Failed to fetch access token"}

    # Convert city names to IATA codes
    origin_iata = get_iata_code(origin_city,access_token)
    destination_iata = get_iata_code(destination_city, access_token)

    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    
    params = {
        "originLocationCode": origin_iata,
        "destinationLocationCode": destination_iata,
        "departureDate": departure_date,
        "adults": adults,
        "children": children,
        "infants": infant,
        "travelClass": travel_class.upper(),
        "currencyCode": currency_code.upper(),
        "maxPrice": max_price,
        "nonStop": "true",
        "max": 1
    }

    # Add returnDate only if it's provided
    if return_date:
        params["returnDate"] = return_date

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return extract_flight_details(response.json())
    else:
        return {"error": f"Failed to fetch flights: {response.json()}"}