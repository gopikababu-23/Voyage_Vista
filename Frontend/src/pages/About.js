import React from "react";
import "./About.css";

const About = () => {
  return (
    <div className="about-container">
      <div className="overlay">
        <h1 style={{ textAlign: "center", color: "greenyellow"}}>About Us - Voyage Vista 🌍✈️</h1>
        <p>
          <strong style={{fontSize:18, color:"white"}}>At Voyage Vista, At Voyage Vista, we believe that travel isn’t just about reaching a destination—it’s about the experiences, the adventures, and the stories that come with it. Whether you're a solo traveler seeking new horizons, a couple planning a romantic getaway, or a group of friends looking for the ultimate adventure, Voyage Vista is here to make your journey smooth, hassle-free, and unforgettable.</strong>
        </p>
        <hr></hr>
        <h2>Who We Are</h2>
        <p style={{fontSize:18, color:"white"}}>
          <strong>Voyage Vista is more than just a travel planner—it’s your personalized travel assistant. We combine cutting-edge technology with expert insights to help travelers explore the world with ease. Our mission is to simplify travel planning by offering an intuitive platform that caters to every type of traveler, from budget backpackers to luxury seekers.</strong>
        </p>
        <hr></hr>
        <h2>What We Offer</h2>
        <ul className="features-list">
          <li>💡 <strong>Custom Itineraries – Say goodbye to one-size-fits-all trips! Our AI-powered system helps you craft a trip based on your interests, budget, and timeline.</strong></li>
          <li>📍 <strong>Smart Travel Planning – We analyze travel trends, best routes, and hidden gems to give you the most optimized plan.</strong></li>
          <li>🎟 <strong>Seamless Booking – Flights, hotels, local transport, and experiences—all in one place!</strong></li>
          <li>💰 <strong>Real-Time Expense Tracking – Stay within budget with our intuitive tracking tool.</strong></li>
          <li>🗺 <strong>Interactive Maps & Navigation – Get guided recommendations on places to visit, dine, and explore.</strong></li>
          <li>👥 <strong>Community & Reviews – Connect with fellow travelers, read real experiences, and make informed decisions.</strong></li>
        </ul>
        <hr></hr>
        <h2>Why Choose Voyage Vista?</h2>
        <ul className="why-us">
          <li>🚀 <strong>Effortless Travel Planning – No more overwhelming research! Let us handle the details while you focus on the excitement.</strong></li>
          <li>🌎 <strong>Explore Like a Local – Find hidden gems, offbeat locations, and authentic cultural experiences tailored just for you.</strong></li>
          <li>🔄 <strong>Ultimate Flexibility – Change your plans on the go and update your itinerary in real-time.</strong></li>
          <li>📊 <strong>Data-Driven Insights – Get smart recommendations based on weather, peak seasons, and tourist trends.</strong></li>
        </ul>
        <hr></hr>
        <p style={{ textAlign: "center", color: "greenyellow", fontSize:20}}><strong>At Voyage Vista, we are on a mission to revolutionize the way people travel. Whether you prefer a meticulously planned itinerary or a spontaneous getaway, we’re here to turn your dream trip into reality.</strong></p>


        <p className="closing-text" style={{ textAlign: "center", color: "greenyellow", fontSize:20}}>
        <strong>💫 Your adventure starts with VoyageVista. Let's explore the world together! 🌍✨</strong>
        </p>
      </div>
    </div>
  );
};

export default About;
