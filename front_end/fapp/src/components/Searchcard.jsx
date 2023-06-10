import React, { useRef } from "react";
import Card from "react-bootstrap/Card";
import "../styles/Searchcard.css";

function Card2() {
  return (
    <div className="rechargephoto">
      <form action=''classname='flex'>
        <div classname='box'>
          <span>City</span>
            <input type='text'placeholder='City'/>
            </div>
        <div classname='box'>
          <span>place</span>
            <input type='text'placeholder='Place'/>
            </div>
      </form>
    </div>
  );
}

export default Card2;