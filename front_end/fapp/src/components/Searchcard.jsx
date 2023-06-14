import React from "react";
import Card from "react-bootstrap/Card";
import "../styles/Searchcard.css";

function Card2() {
  return (
    <div className="rechargephoto">
      <h2 className="search-heading">Real estate search just a click away</h2> {/* Updated heading */}
      <form action='' className='flex'>
        <div className='box'>
          <input type='text' name='city' placeholder='City' />
        </div>
        <div className='box'>
          <input type='text' name='place' placeholder='Place' />
        </div>
        <button type="submit" className="search-button">Search</button>
      </form>
    </div>
  );
}

export default Card2;
