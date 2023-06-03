import React, { useRef } from "react";
import "./Navbar.css";
import { FaShoppingCart, FaBars } from "react-icons/fa";

const Navbar = () => {
  const searchRef = useRef(null);

  const handleSearch = (e) => {
    e.preventDefault();
    const searchValue = searchRef.current.value;
    // Perform search logic
    console.log("Searching for:", searchValue);
    searchRef.current.value = ""; // Clear the search box after search
  };

  return (
    <nav>
      <input type="checkbox" id="check" />
      <label htmlFor="check" className="checkbtn">
        <FaBars />
      </label>
      <label className="logo">Putatoe</label>
      <ul>
        <li><a className="active" href="#">Home</a></li>
        <li><a href="#">Profile</a></li>
        <li><a href="#">Follow list</a></li>
        <li><a href="#">Chat</a></li>
        <li><a href="#">Contact</a></li>
        <li className="search-box">
          <form onSubmit={handleSearch}>
            <input ref={searchRef} type="text" placeholder="Search..." />
            <button type="submit">Search</button>
          </form>
        </li>
        <button className="cart-button">
          <FaShoppingCart className="cart-icon" />
        </button>
      </ul>
    </nav>
  );
};

export default Navbar;