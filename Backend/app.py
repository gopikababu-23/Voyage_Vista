from flask import Flask, request, jsonify
from flask_cors import CORS
from scripts.flight import get_flights
from scripts.hotel import get_best_hotel
import scripts.car as car
import scripts.rental as rental
import scripts.bus as bus
import scripts.gemini as gemini

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# ✅ Default route to check if Flask is running
@app.route('/')
def home():
    return "Flask Backend is Running!"

# ✅ API to Get Flight Details
@app.route("/api/flights", methods=["POST"])
def fetch_flights():
    try:
        data = request.get_json()

        required_fields = ["origin","destination","start_date", "end_date", "adults","children","infants","transport_max", "transport_class","currency_code"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        flight_data = get_flights(
            data["origin"], data["destination"], 
            data["start_date"], data["end_date"], data["adults"],data["children"],data["infants"], data["transport_max"], data["transport_class"], data["currency_code"]
        )
        return jsonify(flight_data)  # ✅ Send JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 🔴 Handle errors

# ✅ API to Get Hotel Details
@app.route("/api/hotels", methods=["POST"])
def api_get_best_hotel():
    try:
        data = request.get_json()

        required_fields = ["destination", "radius", "rating", "hotel_min", "hotel_max", "start_date", "end_date"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        hotel_data = get_best_hotel(
            data["destination"], int(data["radius"]), int(data["rating"]),
            int(data["hotel_min"]), int(data["hotel_max"]),
            data["start_date"], data["end_date"]
        )

        return jsonify(hotel_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ API to Get Car Details
@app.route('/api/car', methods=['POST'])
def get_car():
    data = request.json
    response = car.generate_itinerary_car(data["origin"], data["destination"])
    return jsonify(response)

# ✅ API to Get Rental Details
@app.route('/api/rental', methods=['POST'])
def get_rental():
    data = request.json
    response = rental.generate_itinerary_rental(data["origin"], data["destination"])
    return jsonify(response)

# ✅ API to Get Bus Details
@app.route('/api/bus', methods=['POST'])
def get_bus():
    data = request.json
    response = bus.generate_itinerary_bus(data["origin"], data["destination"], data["transport_class"], data["members"])
    return jsonify(response)

# ✅ API to Generate Complete Itinerary (Gemini AI)
@app.route("/api/generate_itinerary", methods=["POST"])
def generate_itinerary():
    data = request.json  # Get JSON input from frontend
    response_text = gemini.get_full_itinerary(data)  # Call function

    return response_text  # 🔥 Return plain text instead of JSON

if __name__ == '__main__':
    app.run(debug=True)
