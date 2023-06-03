import React, { useRef } from "react";
import "./Navbar.css";

const Navbar = () => {
  const searchRef = useRef(null);

  return (
    <nav>
      <label className="logo">Website</label>
      <ul>
        <li><a href="#">Login / create account</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;