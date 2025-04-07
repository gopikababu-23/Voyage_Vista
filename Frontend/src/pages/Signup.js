import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./signup.css"; // Import the CSS file

const Signup = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    document.body.classList.add("signup-page");
    return () => {
      document.body.classList.remove("signup-page"); // Remove class when leaving page
    };
  }, []);

  const handleSignup = (e) => {
    e.preventDefault();
    alert(`Signed up with Email: ${email}`);
  };

  return (
    <div className="auth-container">
      <h1>Join Us! 🎉</h1>
      <p className="tagline" style={{fontSize: "18px", fontWeight:"bold"}}>Start planning your dream trips with VoyageVista!</p>

      <form onSubmit={handleSignup}>
        <input
          type="text"
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Enter your password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">Sign Up</button>
      </form>

      <p className="login-link" style={{ fontSize: "20px", color:"white", fontWeight:"bold"}}>
        Already have an account? <Link to="/login" style={{ color: "greenyellow"}}>Login here</Link>
      </p>
    </div>
  );
};

export default Signup;
