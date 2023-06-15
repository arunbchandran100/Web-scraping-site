import React from "react";
import "../styles/Searchcard.css";
import { useNavigate } from "react-router-dom";

function Card2() {
  const navigate = useNavigate()
  

  return (
    <div className="rechargephoto">
      <h2 className="search-heading">Real estate search just a click away</h2>
      <form onSubmit={()=>navigate("/search")} className="flex">
        <div className="box">
          <input type="text" placeholder="City" />
        </div>
        <div className="box">
          <input type="text" placeholder="Place" />
        </div>
        <button type="submit" className="search-button">
          Search
        </button>
      </form>
    </div>
  );
}

export default Card2;
