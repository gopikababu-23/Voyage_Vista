import React from "react";
import { Link } from "react-router-dom";
import "./Home.css";

const Home = () => {
  const packages = [
    {
      id: 1,
      name: "Maldives Getaway 🏞️🏝️",
      Duration: "5 Days / 4 Nights",
      Price: "₹59,999 per person",
      image: "https://cdn1.matadornetwork.com/blogs/1/2021/05/maldives-resorts-2.jpg",
      pdf: "/pdf/maldives.pdf",
    },
    {
      id: 2,
      name: "European Adventure 🌍✈️",
      Duration: "7 Days / 8 Nights",
      Price: "₹1,19,999 per person",
      image: "https://st.depositphotos.com/1766887/1831/i/950/depositphotos_18310423-stock-photo-travel-in-europe.jpg",
      pdf: "pdf/Europe.pdf",
    },
    {
      id: 3,
      name: "Himalayan Trek 🌄🏕️",
      Duration: "5 Days / 4 Nights",
      Price: "₹35,499 per person",
      image: "https://images.livemint.com/img/2022/05/20/original/Big_Story_Himalayan_Treks_Nepal_1653055597386.jpg",
      pdf: "/pdf/himalaya.pdf",
    },
    {
      id: 4,
      name: "Wayanad Wonders ❄️🏔️",
      Duration: "3 Days / 2 Nights",
      Price: "₹29,499 per person",
      pdf: "/pdf/wayanad.pdf",
      image: "https://img.traveltriangle.com/blog/wp-content/uploads/2018/04/104.jpg",
    },
    {
      id: 5,
      name: "Andaman & Nicobar Island Escape 🏝️🌊",
      Duration: "4 Days / 3 Nights",
      Price: "₹35,999 per person",
      pdf: "/pdf/andaman.pdf",
      image: "https://dynamic.tourtravelworld.com/package-images/photo-big/dir_9/241132/116226.jpg",
    },
    {
      id: 6,
      name: "Coorg Coffee Trail ☕🌿",
      Duration: "3 Days / 2 Nights",
      Price: "₹8,999 per person",
      pdf:"/pdf/Coorg.pdf",
      image: "https://www.travelingtoworld.com/wp-content/uploads/2017/01/coorg-tourist-places.jpg",
    },
    {
      id: 7,
      name: "Goa Beach Party Getaway 🎉🏖️",
      Duration: "4 Days / 3 Nights",
      Price: "₹12,499 per person",
      pdf: "/pdf/goa.pdf",
      image: "https://www.fabhotels.com/blog/wp-content/uploads/2019/11/Goa-ilterney-600.jpg",
    },
    {
      id: 8,
      name: "Manali Snow & Adventure Trip ❄️🏔️",
      Duration: "5 Days / 4 Nights",
      Price: "₹14,999 per person",
      pdf: "/pdf/manali.pdf",
      image: "https://www.tripsavvy.com/thmb/zyqX35L3rgFRuVrbGioDKoqPezc=/2121x1414/filters:fill(auto,1)/GettyImages-930881934-5ae56fe48023b90036464e72.jpg",
    },
    {
      id: 9,
      name: "Rishikesh & Haridwar Spiritual Escape 🛕🌊",
      Duration: "3 Days / 2 Nights",
      Price: "₹6,999 per person",
      pdf: "/pdf/Rishikesh.pdf",
      image: "https://www.iumdestination.com/galleryimg/72091831-2.jpg",
    },
    {
      id: 10,
      name: "Jaipur & Udaipur Royal Retreat 👑🏰",
      Duration: "4 Days / 3 Nights",
      Price: "₹13,499 per person",
      pdf: "/pdf/jaipu.pdf",
      image: "https://www.nomadicweekends.com/wp-content/uploads/2019/01/Rajasthan-Jaipur-Hawamahal-1200x800.jpg",
    },
    {
      id: 11,
      name: "Kashmir Paradise Tour 🌸🏔️",
      Duration: "6 Days / 5 Nights",
      Price: "₹18,999 per person",
      pdf: "/pdf/kashmir.pdf",
      image: "https://www.stylewithglamour.com/wp-content/uploads/2023/01/wgwgwg.jpg",
    },
    {
      id: 12,
      name: "North East Wonders (Meghalaya & Kaziranga) 🏕️🌲",
      Duration: "5 Days / 4 Nights",
      Price: "₹15,999 per person",
      pdf: "/pdf/north east.pdf",
      image: "https://www.godigit.com/content/dam/godigit/directportal/en/contenthm/nohkalikai-waterfall-cherrapunji.jpg",
    },
    {
      id: 13,
      name: "Spiti Valley Road Trip 🚗🏔️",
      Duration: "7 Days / 6 Nights",
      Price: "₹21,499 per person", 
      pdf: "/pdf/spiti.pdf",
      image: "https://www.lovelytrails.com/admin/assets/uploads/blogs/1625129103.jpg",
    },
    {
      id: 14,
      name: "Singapore City Adventure 🌆🌟",
      Duration: "6 Days / 5 Nights",
      Price: "₹35,999 per person",
      pdf: "/pdf/singapore.pdf",
      image: "https://fthmb.tqn.com/VbuNfLcdgII-GlZYtPDMZoymPBw=/4500x3001/filters:fill(auto,1)/singapore-travel-584f789f5f9b58a8cdf97dda.jpg",
    },
    {
      id: 15,
      name: "Dubai Luxury Escape 🏙️🌟",
      Duration: "5 Days / 4 Nights",
      Price: "₹55,999 per person",
      pdf: "/pdf/dubai.pdf",
      image: "https://www.iabtravel.com/wp-content/uploads/2017/07/DUBAI-COUNTRY-IMAGE-2.jpg",
    },
    {
      id: 16,
      name: "Thailand Budget Getaway 🏖️🐘",
      Duration: "6 Days / 5 Nights",
      Price: "₹38,999 per person",
      pdf:"/pdf/thailand.pdf",
      image: "https://assets-global.website-files.com/5ea992a5dcf9009f68802a74/5ea992a5dcf9002d51803c49_shutterstock_238473214-temple-sunset-wat-none-kum-thailand.jpg",
    },
    {
      id: 17,
      name: "Bali Tropical Paradise 🌊🌴",
      Duration: "5 Days / 4 Nights",
      Price: "₹44,999 per person",
      pdf:"/pdf/bali.pdf",
      image: "https://a.cdn-hotels.com/gdcs/production75/d966/8994658f-13ad-4106-bde4-856450359f47.jpg",
    },
    {
      id: 18,
      name: "Japan Cherry Blossom Tour 🌸🏯",
      Duration: "7 Days / 4 Nights",
      Price: "₹44,999 per person",
      pdf: "/pdf/japan.pdf",
      image: "https://res.cloudinary.com/jnto/image/upload/w_2000,h_1309,c_fill,f_auto,fl_lossy,q_auto/v1/media/filer_public/d4/ce/d4ce9c41-6bfe-4996-a998-271866907abd/02shutterstock_188615729_zynqxa",
    },
    {
      id: 19,
      name: "Malaysia City Adventure 🌆🌟",
      Duration: "6 Days / 5 Nights",
      Price: "₹32,999 per person",
      pdf: "/pdf/malaysia.pdf",
      image: "https://www.brandsynario.com/wp-content/uploads/2017/11/malaysia-travel-696x418.jpg",
    },
    {
      id: 20,
      name: "Leh Ladakh Adventure 🏍️🏔️",
      Duration: "5 Days / 4 Nights",
      Price: "₹52,999 per person",
      pdf: "/pdf/ladakh.pdf",
      image: "https://lp-cms-production.imgix.net/news/2018/04/ladakh.jpg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850",
    },

  ];

  return (
    <div className="home-container">
      <h1 style={{ fontSize: 40, color:"black"}}>Welcome to VoyageVista</h1>
      <p style={{fontSize: 25, color: "black"}}><strong>Explore our exciting travel packages or create your own itinerary!</strong></p>

      <div className="packages">
        {packages.map((pkg) => (
          <div key={pkg.id} className="package-card">
            <img src={pkg.image} alt={pkg.name} />
            <h3>{pkg.name}</h3>
            <p>Starting from {pkg.Price}</p>
            <p>{pkg.Duration}</p>
            {pkg.pdf ? (
              <a
                href={pkg.pdf}
                target="_blank"
                rel="noopener noreferrer"
                className="pack-button"
                style={{ fontSize: "16px", textDecoration: "none", display: "inline-block" }}
              >
                View Details
              </a>
            ) : (
              <button className="pack-button" style={{ fontSize: "16px" }} disabled>
                No Details
              </button>
            )}
          </div>
        ))}
      </div>

      <div className="create-itinerary">
        <h2 style={{color: "black", fontSize: 24}}>Don't like the existing plans? No worries! Create your own custom itinerary just the way you want! ✨🗺️</h2>
        <Link to="/create-itinerary">
          <button style={{ padding: "10px 20px",background: "#349edb",color: "white", fontWeight: "bold", border: "none", borderRadius: "5px" ,cursor: "pointer", fontSize:20}}>Create Your Itinerary</button>
        </Link>
      </div>
    </div>
  );
};

export default Home;
