const express = require("express");
const router = express.Router();
const db = require("../db"); // MySQL connection

router.post("/itinerary", (req, res) => {
    const {
        name, email, phone, origin, destination, start_date, end_date, transport_mode,
        transport_class, adults, children, infants, members, currency_code,
        transport_min, transport_max, hotel_min, hotel_max, other_expenses_min,
        other_expenses_max, rating
    } = req.body;

    const sql = "INSERT INTO itineraries (name, email, phone, origin, destination, start_date, end_date, transport_mode, transport_class, adults, children, infants, members, currency_code, transport_min, transport_max, hotel_min, hotel_max, other_expenses_min, other_expenses_max, rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

    db.query(sql, [name, email, phone, origin, destination, start_date, end_date, transport_mode, transport_class, adults, children, infants, members, currency_code, transport_min, transport_max, hotel_min, hotel_max, other_expenses_min, other_expenses_max, rating], (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).json({ message: "Database error" });
        } else {
            res.status(201).json({ message: "Itinerary saved successfully" });
        }
    });
});

module.exports = router;
