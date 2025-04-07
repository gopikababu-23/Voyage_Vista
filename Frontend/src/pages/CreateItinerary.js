import React, { useState, useEffect } from "react";
import axios from "axios";
import generatePDF from "./generateItinerary";
import "./CreateItinerary.css";

const CreateItinerary = () => {
    const [formData, setFormData] = useState({
        name: "", email: "", phone: "", origin: "", destination: "",
        start_date: "", end_date: "", transport_mode: "", transport_class: "",
        adults: "", children: "", infants: "",members:"", currency_code: "",
        transport_min: "", transport_max: "", hotel_min: "", hotel_max: "",
        other_expenses_min: "", other_expenses_max: "", rating: ""
    });

    const [itinerary, setItinerary] = useState(null);
    const [showItinerary, setShowItinerary] = useState(false);

    
    useEffect(() => {
        document.body.classList.add("create-itinerary-bg");
        return () => {
            document.body.classList.remove("create-itinerary-bg"); // Remove when leaving
        };
    }, []);


    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post(
                "http://127.0.0.1:5000/api/generate_itinerary",
                formData
            );
            console.log("API Response:", response.data);
            setItinerary(response.data); // Store response
            setShowItinerary(true); // Ensure visibility
            alert("Itinerary generated successfully!");
        } catch (error) {
            console.error("Error fetching itinerary:", error);
            alert("Failed to generate itinerary");
        }
    };

    // ✅ Function to generate PDF
    
    return (
        <div className="itinerary-container">
            <h2 style={{ textAlign: "center", color:"greenyellow", fontSize:30}}>Enter your preferences</h2>
            <form onSubmit={handleSubmit}>
                <label style={{ color:"white"}}>Name:</label>
                <input type="text" name="name" value={formData.name} onChange={handleChange} required />

                <label style={{ color:"white"}}>Email ID:</label>
                <input type="email" name="email" value={formData.email} onChange={handleChange} required />

                <label style={{ color:"white"}}>Phone Number:</label>
                <input type="text" name="phone" value={formData.phone} onChange={handleChange} required />

                <label style={{ color:"white"}}>Origin:</label>
                <input type="text" name="origin" value={formData.origin} onChange={handleChange} required />

                <label style={{ color:"white"}}>Destination:</label>
                <input type="text" name="destination" value={formData.destination} onChange={handleChange} required />

                <label style={{ color:"white"}}>Start Date:</label>
                <input type="date" name="start_date" value={formData.start_date} onChange={handleChange} required />

                <label style={{ color:"white"}}>End Date:</label>
                <input type="date" name="end_date" value={formData.end_date} onChange={handleChange} required />

                <label style={{ color:"white"}}>Transport Mode:</label>
                <select name="transport_mode" value={formData.transport_mode} onChange={handleChange} required>
                    <option value="">Select</option>
                    <option value="Bus">Bus</option>
                    <option value="Car">Car</option>
                    <option value="Rental">Rental Car</option>
                    <option value="Flight">Flight</option>
                </select>

                <label style={{ color:"white"}}>Transport Class:</label>
                <select name="transport_class" value={formData.transport_class} onChange={handleChange} required>
                    <option value="">Select</option>
                    <option value="Economy">Economy (Flight)</option>
                    <option value="Business">Business (Flight)</option>
                    <option value="First Class">First Class (Flight)</option>
                    <option value="Sleeper">Sleeper (Bus)</option>
                    <option value="Semi-Sleeper">Semi Sleeper (Bus)</option>
                    <option value="Luxury">Luxury (Bus)</option>
                </select>

                <label style={{ color:"white"}}>Adults:</label>
                <input type="number" name="adults" value={formData.adults} onChange={handleChange} required />

                <label style={{ color:"white"}}>Members:</label>
                <input type="number" name="members" value={formData.adults} onChange={handleChange} required />

                <label style={{ color:"white"}}>Children:</label>
                <input type="number" name="children" value={formData.children} onChange={handleChange} />

                <label style={{ color:"white"}}>Infants:</label>
                <input type="number" name="infants" value={formData.infants} onChange={handleChange} />

                <label style={{ color:"white"}}>Currency Code:</label>
                <input type="text" name="currency_code" value={formData.currency_code} onChange={handleChange} required />

                <label style={{ color:"white"}}>Transport Budget:</label>
                <input type="number" name="transport_min" placeholder="Min" value={formData.transport_min} onChange={handleChange} required />
                <input type="number" name="transport_max" placeholder="Max" value={formData.transport_max} onChange={handleChange} required />

                <label style={{ color:"white"}}>Hotel Budget:</label>
                <input type="number" name="hotel_min" placeholder="Min" value={formData.hotel_min} onChange={handleChange} required />
                <input type="number" name="hotel_max" placeholder="Max" value={formData.hotel_max} onChange={handleChange} required />

                <label style={{ color:"white"}}>Other Expenses:</label>
                <input type="number" name="other_expenses_min" placeholder="Min" value={formData.other_expenses_min} onChange={handleChange} required />
                <input type="number" name="other_expenses_max" placeholder="Max" value={formData.other_expenses_max} onChange={handleChange} required />

                <label style={{ color:"white"}}>Hotel Rating (1-5):</label>
                <input type="number" name="rating" value={formData.rating} onChange={handleChange} required />
                <br></br>
                <button type="submit">Generate Itinerary</button>
            </form>

            {showItinerary && itinerary && (
                <div className="itinerary-output">
                    <div id="itinerary-content" style={{ padding: "20px", background: "white" }}>
                        <h2>Generated Itinerary</h2>
                        <pre style={{whiteSpace: "pre-wrap"}}>{itinerary}</pre>
                    </div>
                    <button onClick={generatePDF}>Download PDF</button>
                </div>
            )}
        </div>
    );
};

export default CreateItinerary;
