import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./login.css"; // Import the CSS file

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    document.body.classList.add("login-page");
    return () => {
      document.body.classList.remove("login-page"); // Remove class when leaving page
    };
  }, []);

  const handleLogin = (e) => {
    e.preventDefault();
    alert(`Logging in with Email: ${email}`);
  };

  return (
    <div className="auth-container">
      <h2 style={{ color: "white", fontSize:"28px"}}>Welcome Back! 🌍✨</h2>
      <p className="tagline" style={{ color: "white", fontWeight: "bold", fontSize: "20px"}}>Plan your next adventure with VoyageVista!</p>
      <form onSubmit={handleLogin}>
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
        <div className="login-options" >
          <Link style={{ color: "greenyellow"}}>
            Forgot Password?
          </Link>
        </div>
        <Link to="/home">
            <button style={{ padding: "10px 20px", fontSize: "18px" }}>Login</button>
        </Link>
      </form>
      <p style={{fontSize: "20px", color:"white", fontWeight:"bold"}}>
        Don't have an account? <Link to="/signup" style={{ color: "greenyellow"}}>Sign up here</Link>
      </p>
    </div>
  );
};

export default Login;
