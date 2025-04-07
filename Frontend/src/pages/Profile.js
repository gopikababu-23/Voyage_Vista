import React, { useState, useEffect } from "react";
import "./Profile.css";

const Profile = () => {
  useEffect(() => {
    document.body.classList.add("profile-page"); // Apply background only for this page
    return () => {
      document.body.classList.remove("profile-page"); // Remove on unmount to avoid affecting other pages
    };
  }, []);

  const [user] = useState({
    name: "Gopika Babu",
    email: "gopibabu@gmail.com",
    location: "Chennai, India",
    joinedDate: "January 2023",
    totalBookings: 5,
    reviews: 12,
    favorites: 8,
    bio: "Travel enthusiast exploring new places & cultures. Passionate about adventure and making unforgettable memories!",
    interests: ["Traveling", "Photography", "Foodie", "Tech Enthusiast"],
    recentTrips: ["🏝️ Maldives Escape", "🏔️ Manali Snow Trek", "🌆 Dubai City Tour"],
    profilePic: "https://wallpapers.com/images/featured/cute-profile-picture-s52z1uggme5sj92d.jpg",
  });

  return (
    <div className="profile-container">
      <div className="profile-card">
        <div className="profile-pic">
          <img src={user.profilePic} alt="Profile" />
          <button className="change-pic-btn">📷 Change</button>
        </div>

        <h1 style={{color:"greenyellow"}}>👋 Hello, {user.name}!</h1>
        <p style={{ color:"white"}}>📧 <strong>Email:</strong> {user.email}</p>
        <p style={{ color:"white"}}>📍 <strong>Location:</strong> {user.location}</p>
        <p style={{ color:"white"}}>📅 <strong>Member Since:</strong> {user.joinedDate}</p>

        <div className="bio">
          <h3>About Me</h3>
          <p>{user.bio}</p>
        </div>

        <div className="interests">
          <h3 style={{ color:"white"}}>Interests</h3>
          <div className="tags">
            {user.interests.map((interest, index) => (
              <span key={index} className="tag">{interest}</span>
            ))}
          </div>
        </div>

        <div className="profile-stats">
          <div>
            <h2>{user.totalBookings}</h2>
            <p>Total Bookings</p>
          </div>
          <div>
            <h2>{user.reviews}</h2>
            <p>Reviews & Ratings</p>
          </div>
          <div>
            <h2>{user.favorites}</h2>
            <p>Saved Items</p>
          </div>
        </div>

        <div className="recent-trips" >
          <h3 style={{ color:"white"}}>Recent Trips</h3>
          <ul>
            {user.recentTrips.map((trip, index) => (
              <li key={index}>{trip}</li>
            ))}
          </ul>
        </div>

        <div className="profile-actions">
          <button className="edit-btn">✏️ Edit Profile</button>
          <button className="settings-btn">⚙️ Account Settings</button>
          <button className="logout-btn">🚪 Logout</button>
        </div>
      </div>
    </div>
  );
};

export default Profile;
