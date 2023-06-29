import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Searchcard.css";
import {useNavigate} from "react-router-dom"

function Card2() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    city: "",
    place: "",
  });
  const navigate = useNavigate()
  const handleSubmit = (event) => {
    event.preventDefault();


    // Send the POST request to the Django API endpoint
    fetch("http://127.0.0.1:8000/subapp/form/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
<<<<<<< Updated upstream
      // .then(navigate("/search"))
      .then((response) => response.json())
=======
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Request failed");
        }
      })
>>>>>>> Stashed changes
      .then((data) => {
        console.log(data);

        // Handle the response from the Django API
        navigate("/search")

      
        // ...

        // Navigate to the "/search" page
        navigate("/search");
      })
      .catch((error) => {
        // Handle any error that occurred during the API request
        console.error(error);
        // ...
      });
  };

  const handleChange = (event, name) => {
    const { value } = event.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  return (
    <div className="rechargephoto">
<<<<<<< Updated upstream
      <h2 className="search-heading">Real estate search just a click away</h2> {/* Updated heading */}
    <form onSubmit={handleSubmit}>
      {/* Your form inputs */}
      <div className='box'>
      <input
        type="text"
        name="city"
        value={formData.city}
        onChange={(e)=>handleChange(e,"city")}
        placeholder='City'
      />
      </div>
      <div className='box'>
      <input
        type="text"
        name="place"
        value={formData.place}
        onChange={(e)=>handleChange(e,"place")}
        placeholder='Place'
      />
      {/* ... */}

      </div>
       <button type="submit" className="search-button">Search</button>
    </form>
=======
      <h2 className="search-heading">Real estate search just a click away</h2>
      <form onSubmit={handleSubmit}>
        <div className="box">
          <input
            type="text"
            name="city"
            value={formData.city}
            onChange={(e) => handleChange(e, "city")}
            placeholder="City"
          />
        </div>
        <div className="box">
          <input
            type="text"
            name="place"
            value={formData.place}
            onChange={(e) => handleChange(e, "place")}
            placeholder="Place"
          />
        </div>
        <button type="submit" className="search-button">
          Search
        </button>
      </form>
>>>>>>> Stashed changes
    </div>
  );
}

export default Card2;
