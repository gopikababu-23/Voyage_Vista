import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Logout = () => {
  const navigate = useNavigate();

  useEffect(() => {
    // Remove user authentication data (if stored in localStorage)
    localStorage.removeItem("user");
    localStorage.removeItem("token");

    // Redirect to login page after logout
    navigate("/login");
  }, [navigate]);

  return null; // No need to display anything
};

export default Logout;
