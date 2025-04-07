import React from "react";
import { Link } from "react-router-dom";
import "./getStarted.css";

const GetStarted = () => {
  return (
    <div className="hero-container">
      <div className="hero-content">
        <h1 style={{ fontSize: "60px" , color: "#00416a"}}>Let's Enjoy The Wonders of Nature</h1>
        <p className="description" style={{ color: "#0f4d92 ", fontSize:"21px", fontWeight:"bold", fontFamily: "serif"}}>
        Plan your dream journey with VoyageVista, your ultimate travel companion! Explore breathtaking destinations, customize your itinerary to match your preferences, and enjoy a stress-free adventure. With AI-powered recommendations and real-time budgeting, we ensure a seamless and unforgettable travel experience tailored just for you.
        </p>
        <p style={{ color: "#0f4d92 ", fontSize:"21px", fontWeight:"bold", fontFamily: "serif"}}><strong>Ready to begin? Click Get Started and let’s turn your travel dreams into reality!</strong></p>
        <br></br>
        <Link to="/Login">
          <button className="hero-btn">Get Started</button>
        </Link>
      </div>
    </div>
  );
};

export default GetStarted;
