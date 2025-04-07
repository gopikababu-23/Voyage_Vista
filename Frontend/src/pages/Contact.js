import React, { useState } from "react";
import "./Contact.css";

const Contact = () => {
  const [formData, setFormData] = useState({ name: "", email: "", message: "" });
  const [confirmation, setConfirmation] = useState("");

  const validateEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validateEmail(formData.email)) {
      alert("Please enter a valid email address.");
      return;
    }
    setConfirmation("Message sent successfully! ✅");
    setTimeout(() => setConfirmation(""), 3000);
    setFormData({ name: "", email: "", message: "" });
  };

  return (
    <div className="contact-container">
      {/* Background Image */}
      <div className="contact-bg"></div>
      
      <div className="contact">
        <h3 style={{ textAlign: "center", color:"greenyellow"}}>We’d love to hear from you! Whether you have questions, feedback, or need assistance, feel free to reach out to us. Our team is always ready to help!</h3>
        <h3 style={{ textAlign: "center"}}><strong>📍 Our Location: 123, Main Street, Chennai, India</strong></h3>
        <h3 style={{ textAlign: "center"}}><strong>📞 Phone: +91 98765 43210</strong></h3>
        <h3 style={{ textAlign: "center"}}><strong>📧 Email: support@yourwebsite.com</strong></h3>
        <h3 style={{ textAlign: "center"}}><strong>🕒 Working Hours:</strong></h3>
        <h3 style={{ textAlign: "center"}}>Monday – Friday: 9:00 AM – 6:00 PM</h3>
        <h3 style={{ textAlign: "center"}}>Saturday: 10:00 AM – 4:00 PM</h3>
        <h3 style={{ textAlign: "center"}}>Sunday: Closed</h3>
        <h3 style={{ textAlign: "center", color:"greenyellow"}}><strong>💬 Get in Touch</strong></h3>
        <h3 style={{ textAlign: "center", color:"greenyellow"}}>Fill out the form below, and we’ll get back to you as soon as possible.</h3>
        <form className="contact-form" onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Your Name"
            required
            value={formData.name}
            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
          />
          <input
            type="email"
            placeholder="Your Email"
            required
            value={formData.email}
            onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          />
          <textarea
            placeholder="Your Message"
            required
            value={formData.message}
            onChange={(e) => setFormData({ ...formData, message: e.target.value })}
          ></textarea>
          <button type="submit">Send Message</button>
        </form>
        <br />
        {confirmation && <p className="confirmation">{confirmation}</p>}
      </div>
    </div>
  );
};

export default Contact;
