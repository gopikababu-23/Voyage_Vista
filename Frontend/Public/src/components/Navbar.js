import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Navbar.css"; // Importing styles

const Navbar = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("user");
    localStorage.removeItem("token");
    navigate("/login"); // Redirect to login page
  };

  return (
    <nav className="navbar">
      <h1 className="logo">VoyageVista</h1>
      <ul className="nav-links">
        <li><Link to="/home">Home</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/create-itinerary">Create Itinerary</Link></li>
        <li><Link to="/faq"> FAQ</Link></li>
        <li><Link to="/contact">Contact Us</Link></li>
        <li><Link to="/profile">Profile</Link></li>
        
        <li>
          <button onClick={handleLogout} className="logout-btn">Logout</button>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;

