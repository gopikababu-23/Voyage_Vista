import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./faq.css";

const FAQ = () => {
  const [openFAQs, setOpenFAQs] = useState([]);

  useEffect(() => {
    document.body.classList.add("faq-page");
    return () => {
      document.body.classList.remove("faq-page");
    };
  }, []);

  const toggleAnswer = (index) => {
    setOpenFAQs((prev) =>
      prev.includes(index) ? prev.filter((i) => i !== index) : [...prev, index]
    );
  };


  const faqs = [
    { question: "What is Voyage Vista?", answer: "Voyage Vista is a smart travel planning platform designed to help travelers create personalized itineraries, find the best travel deals, track expenses, and explore destinations seamlessly. Whether you're planning a solo trip, a family vacation, or an adventurous getaway, we’ve got you covered!" },
    { question: "How does Voyage Vista work?", answer: "Our platform allows you to choose from pre-made travel packages or create a custom itinerary based on your interests, budget, and schedule. Simply enter your destination, preferences, and travel dates, and Voyage Vista will generate a tailored plan with recommended attractions, accommodations, and activities." },
    { question: "Can I customize my travel itinerary?", answer: "Absolutely! Voyage Vista provides complete flexibility to modify your itinerary. You can add or remove destinations, change accommodations, and even adjust travel routes to suit your preferences." },
    { question: "Does Voyage Vista offer real-time expense tracking?", answer: "Yes! Our expense tracking feature helps you stay within budget by monitoring your spending on flights, hotels, food, activities, and more. This ensures a stress-free travel experience." },
    { question: "Can I book flights and hotels directly through Voyage Vista?", answer: "Yes, Voyage Vista provides seamless booking options for flights, hotels, and experiences through our trusted travel partners, making it easy to manage everything in one place." },
    { question: "Is Voyage Vista available for international trips?", answer: "Of course! Whether you’re planning a trip within your country or exploring international destinations, Voyage Vista offers recommendations and insights for worldwide travel." },
    { question: "Does Voyage Vista offer travel recommendations and local insights?", answer: "Yes! Our platform suggests must-visit attractions, hidden gems, and local experiences based on your travel style and preferences. We also provide real-time updates on weather, safety tips, and cultural insights."},
    { question: "Is Voyage Vista free to use?", answer: "Yes, Voyage Vista offers a free version with essential travel planning tools. However, for access to premium features like AI-powered recommendations, exclusive discounts, and advanced itinerary management, we offer a Voyage Vista Pro subscription." },
    { question: "Can I share my itinerary with friends and family?", answer: "Yes! Voyage Vista allows you to share your itinerary with fellow travelers or family members, making group travel planning seamless and fun." },
    { question: "What if I need to change my travel plans?", answer: "No worries! You can edit your itinerary anytime, rebook accommodations, or adjust your trip details with ease through our platform." },
    { question: "How do I get customer support?", answer: "We’re here to help! You can reach out to our support team through the in-app chat, email, or our 24/7 helpline for any travel-related assistance." },
    { question: "How do I get started with Voyage Vista?", answer: "Simply sign up, enter your travel details, and let Voyage Vista do the magic! Click “Get Started” to begin planning your next adventure today." },
  ];

  return (
    <div className="faq-container">
  
      <h2 style={{ textAlign: "center", color: "greenyellow", fontSize: 30}}>Frequently Asked Questions</h2>
      {faqs.map((faq, index) => (
        <div key={index} className={`faq ${openFAQs.includes(index) ? "active" : ""}`}>
          <h3 onClick={() => toggleAnswer(index)}>
            {index + 1}. {faq.question}
          </h3>
          {openFAQs.includes(index) && <p>{faq.answer}</p>}
        </div>
      ))}
      <div className="create-itinerary">
        <p style={{ textAlign: "center", color: "greenyellow", fontSize: 20}}>
            <strong>💫 Still have questions? Feel free to contact us—we’re happy to help! ✨</strong>
        </p>
        <Link to="/contact"> {/* Changed from "/faq" to "/contact" for clarity */}
          <button className="create-btn" style={{ alignItems:"center", fontWeight:"bold" }}>Contact</button> 
        </Link>
      </div>
    </div>
  );
};

export default FAQ;