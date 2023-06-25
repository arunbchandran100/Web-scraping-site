import React, { useState } from "react";
import Card from "react-bootstrap/Card";
import "../styles/Searchcard.css";

function Card2() {
  const [formData, setFormData] = useState({
    // Initialize form data here
    name: "",
    email: "",
    // ...
  });

  const handleSubmit = (event) => {
    event.preventDefault();

    // Send the POST request to the Django API endpoint
    fetch("/api/submit_form/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the Django API
        console.log(data);
        // ...
      })
      .catch((error) => {
        // Handle any error that occurred during the API request
        console.error(error);
        // ...
      });
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  return (
    <div className="rechargephoto">
      <h2 className="search-heading">Real estate search just a click away</h2> {/* Updated heading */}
    <form onSubmit={handleSubmit}>
      {/* Your form inputs */}
      <input
        type="text"
        name="city"
        value={formData.name}
        onChange={handleChange}
      />
      <input
        type="text"
        name="place"
        value={formData.email}
        onChange={handleChange}
      />
      {/* ... */}
       <button type="submit" className="search-button">Search</button>
    </form>
    </div>
  );
}

export default Card2;
