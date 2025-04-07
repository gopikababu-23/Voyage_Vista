import absl.logging
from google import genai
import json
from .flight import get_flights
from .car import generate_itinerary_car
from .bus import generate_itinerary_bus
from .hotel import get_best_hotel
from .rental import generate_itinerary_rental

absl.logging.set_verbosity(absl.logging.ERROR)

# Set up Gemini AI API Key
client= genai.Client(api_key="")

def generate_itinerary(user_input):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""Generate a detailed travel itinerary report (2000 - 3000 words) based on the user's input below:
        {json.dumps(user_input, indent=4)}
        ✅ Mandatory Requirements:
            ✔ Strictly follow the output format.
            ✔ Time slots (6:00 AM - 7:00 AM format) for all activities.
            ✔ Distance & travel time must be included for all travel.
            ✔ Start date and end date has to be included for all travels.
            ✔ Visit 5 places for each day.
            ✔ Transport details vary based on the mode: 
                Car/Rental Cars: ❌ No cab/auto fares needed, 
                                ✅ Include only distance, time, and parking fees.
                Bus/Flight: ✅ Include cab/auto fares, distance, time, and cost (per person & total).
            ✔ Parking fees apply only to cars/rental cars.
            ✔ Return journey must be included on the last day to thr origin. That's it.
            ✔ Real-time budget breakdown in table format.
            ✔ Shopping must be included on the last day or the day before.
            ✔ All expenses: transport, hotel, entry fees, local travel.
            ✔ Total savings calculation from allocated budget.
            ✔ For input Budget use maximum budget.
            ✔ Brief description of all places visited.
            ✔ Print "Have a happy journey!" at the end.

        🔹 Output Format:
            1. User Details:Name, Email, Phone Number,Origin & Destination,Travel Dates (Start & End),Transport Mode, Number of Adults, Currency Code, Hotel Rating
            2. Detailed Itinerary (Day-wise with Time Slots & Place Descriptions)
                ✅ Time format: 6:00 AM - 7:00 AM
                ✅ Distance & travel time for each trip
                ✅ Entry fees, parking charges (only for car/rental cars), and total cost for every activity
                ✅ Brief descriptions of tourist attractions

        Example:
            📅 Day 1: Arrival & Local Sightseeing
            Flight Travel Itinerary
                🚗 6:00 AM - 7:00 AM → Drive from Home to Airport (10 km, 20 mins, Parking Fee: ₹100)
                ✈ 8:00 AM - 10:30 AM → Flight from Chennai to Delhi (₹5,000/person, ₹10,000 total)
                🚑 11:00 AM - 11:30 AM → Cab from Airport to Hotel (15 km, 40 mins, ₹500 total)
                🏨 12:00 PM → Check-in at XYZ Hotel
                🍽️ 1:00 PM - 2:00 PM → Lunch at ABC Restaurant (₹250/person, ₹500 total)
                🚗 2:30 PM - 3:30 PM → Travel to India Gate (5 km, 15 mins)🏙️ 3:30 PM - 5:00 PM → Explore India Gate (Entry Fee: ₹50/person, ₹100 total)
                    🏙️ About the Place:India Gate is a war memorial built in honor of the soldiers who fought in World War I. The 42-meter-high structure is one of Delhi’s most famous landmarks and a great place for photography and evening strolls.
                🚗 5:30 PM - 6:30 PM → Travel to Lotus Temple (10 km, 30 mins)🏙️ 6:30 PM - 7:30 PM → Visit Lotus Temple (Entry: Free)
                    🏙️ About the Place:The Lotus Temple is a Baháʼí House of Worship, known for its stunning architecture that resembles a lotus flower. It is a peaceful place for meditation and spiritual reflection.
                🛍️ 8:00 PM - 9:30 PM → Shopping at Sarojini Market (Approx. ₹1,000)
                🍽️ 9:30 PM - 10:30 PM → Dinner at DEF Restaurant (₹300/person, ₹600 total)
                🏨 11:00 PM → Return to Hotel & Rest


            📅 Day 1: Arrival & Local Sightseeing
            🚍 Bus Travel Itinerary
                🔹 6:00 AM - 6:30 AM → Cab from Home to Bus Station (10 km, 30 mins, ₹200)
                🔹 7:00 AM - 1:00 PM → Bus from Chennai to Pondicherry (170 km, 6 hrs, ₹350/person, ₹700 total)
                🔹 1:30 PM - 2:00 PM → Auto from Bus Station to Hotel (5 km, 15 mins, ₹150 total)
                🔹 2:00 PM → Check-in at XYZ Hotel (3-star, ₹3,000/night)
                🔹 2:30 PM - 3:30 PM → Lunch at ABC Restaurant (₹300/person, ₹600 total)
                🔹 4:00 PM - 4:30 PM → Auto to Paradise Beach (6 km, 20 mins, ₹200 total)
                🔹 4:30 PM - 6:00 PM → Enjoy at Paradise Beach (Entry Fee: ₹150/person, ₹300 total)
                🏝️ About the Place: Paradise Beach is one of the cleanest and most scenic beaches in Pondicherry, known for its soft golden sand and calm waters. Perfect for relaxing and photography.
                🔹 6:30 PM - 7:00 PM → Auto to Promenade Beach (8 km, 25 mins, ₹250 total)
                🔹 7:00 PM - 8:00 PM → Walk along Promenade Beach (Free)
                🔹 8:30 PM - 9:30 PM → Dinner at XYZ Café (₹400/person, ₹800 total)
                🔹 10:00 PM → Return to Hotel & Rest

            📅 Day 1: Arrival & Local Sightseeing
            🚗 Car/Rental Car Travel Itinerary
                🔹 6:00 AM - 6:15 AM → Drive from Home to Rental Car Pickup (5 km, 15 mins, Parking Fee: ₹50)
                🔹 6:30 AM - 10:30 AM → Drive from Chennai to Pondicherry (170 km, 4 hrs, Fuel Cost: ₹1,200)
                🔹 11:00 AM → Check-in at XYZ Hotel (3-star, ₹3,000/night, Parking Fee: ₹100)
                🔹 12:30 PM - 1:30 PM → Lunch at ABC Restaurant (₹300/person, ₹600 total)
                🔹 2:00 PM - 2:30 PM → Drive to Auroville (12 km, 30 mins)
                🔹 2:30 PM - 4:00 PM → Explore Auroville (Free Entry)
                🌱 About the Place: Auroville is an experimental township promoting unity and sustainable living. The highlight is the golden Matrimandir, a meditation center with a futuristic design.
                🔹 4:30 PM - 5:00 PM → Drive to Paradise Beach (10 km, 30 mins, Parking Fee: ₹50)
                🔹 5:00 PM - 6:30 PM → Enjoy at Paradise Beach (Entry Fee: ₹150/person, ₹300 total)
                🔹 7:00 PM - 7:30 PM → Drive to White Town (5 km, 15 mins)
                🔹 7:30 PM - 8:30 PM → Evening Walk at Promenade Beach (Free)
                🔹 9:00 PM - 10:00 PM → Dinner at XYZ Café (₹400/person, ₹800 total)
                🔹 10:30 PM → Return to Hotel & Rest
                   
            3. Budget Breakdown (Table Format - Mandatory)
                Expense Type    Input Budget    Spent     Saved
                Transport       ₹XXXX           ₹XXXX     ₹XXXX
                Accommodation   ₹XXXX           ₹XXXX     ₹XXXX
                Other Expenses  ₹XXXX           ₹XXXX     ₹XXXX
                Total           ₹XXXX           ₹XXXX     ₹XXXX

            4. Transport Details: onward and return
            5. Hotel Details
            6. Notes
            7. Final Summary: Mention total saved amount from the allocated budget.
            8. Final Message:📢 "Have a happy journey!"

        Execution Rules:
            ✅ Strictly follow the output format.
            ✅ Time slots (6:00 AM - 7:00 AM format) are compulsory.
            ✅ Descriptions for all tourist places are mandatory.
            ✅ Parking fees apply only for cars/rental cars, not for buses/flights.
            ✅ Return journey must be fully included.
            ✅ Last Date must be included for all travels
            ✅ Mention Day, date and title are mandatory
            ✅ Departure is only on the last date.
            ✅ Follow the example format.
            ✅ Provide the itinerary only within the start date(included) and end date(included). 
            
        other expenses = entry fees, parking fees, cab/auto/metro charges
        """
    )
    return response.text.strip()

def get_full_itinerary(data):
    user_input = {
        "name": data["name"],
        "email": data["email"],
        "phone": data["phone"],
        "origin": data["origin"],
        "destination": data["destination"],
        "start_date": data["start_date"],
        "end_date": data["end_date"],
        "transport_mode": data["transport_mode"],
        "transport_class": data.get("transport_class", ""),
        "adults": data["adults"],
        "children": data["children"],
        "infants": data["infants"],
        "members": data["members"],
        "currency_code": data["currency_code"],
        "rating": data["rating"],
        "budget": {
            "transport_min": data["transport_min"],
            "transport_max": data["transport_max"],
            "hotel_min": data["hotel_min"],
            "hotel_max": data["hotel_max"],
            "other_expenses_min": data["other_expenses_min"],
            "other_expenses_max": data["other_expenses_max"]
        }
    }

    # 🔹 Fetch transport details dynamically
    if user_input["transport_mode"] == "Flight":
        flight_details = get_flights(
            user_input["origin"], user_input["destination"], user_input["start_date"],
            user_input["end_date"], user_input["adults"], user_input["children"],
            user_input["infants"], user_input["budget"]["transport_max"], user_input["transport_class"], user_input["currency_code"]
        )
        user_input["onward_transport_details"] = flight_details.get("onward_flight", {})
        user_input["return_transport_details"] = flight_details.get("return_flight", {})

    elif user_input["transport_mode"] == "Bus":
        user_input["onward_transport_details"] = generate_itinerary_bus(
            user_input["origin"], user_input["destination"], user_input["transport_class"], user_input["members"]
        )
        user_input["return_transport_details"] = generate_itinerary_bus(
            user_input["destination"], user_input["origin"], user_input["transport_class"], user_input["members"]
        )

    elif user_input["transport_mode"] == "Car":
        user_input["onward_transport_details"] = generate_itinerary_car(user_input["origin"], user_input["destination"])
        user_input["return_transport_details"] = generate_itinerary_car(user_input["destination"], user_input["origin"])

    elif user_input["transport_mode"] == "Rental":
        user_input["onward_transport_details"] = generate_itinerary_rental(user_input["origin"], user_input["destination"])
        user_input["return_transport_details"] = generate_itinerary_rental(user_input["destination"], user_input["origin"])

    # 🔹 Fetch hotel details dynamically
    hotel_details = get_best_hotel(
        user_input["destination"], 20, user_input["rating"],
        user_input["budget"]["hotel_min"], user_input["budget"]["hotel_max"],
        user_input["start_date"], user_input["end_date"]
    )

    if "error" in hotel_details:
        print(f"❌ Hotel API Error: {hotel_details['error']}")
        user_input["hotel_name"] = "Hotel details unavailable"
        user_input["rating"] = "N/A"
        user_input["price_per_night"] = "N/A"
        user_input["Booking_Link"] = "N/A"
        user_input["Total_Price_to_stay"] = "N/A"
    else:
        user_input["hotel_name"] = hotel_details["name"]
        user_input["rating"] = hotel_details["rating"]
        user_input["price_per_night"] = hotel_details["price_per_night"]
        user_input["Booking_Link"] = hotel_details["booking_link"]
        user_input["Total_Price_to_stay"] = hotel_details["total_cost"]
    # Generate Itinerary using AI
    itinerary_report = generate_itinerary(user_input)

    return itinerary_report