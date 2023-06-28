import React from "react";
import Searchcard from "../components/Searchcard";
import Footer from "../components/Footer";
import Navbar from "../components/Navbar";
import Product from "../components/product";
import "../styles/SearchPage.css"
function SearchPage() {
  return (
    <div className="Home">
      <Navbar />
      <Product/>
      <Footer />
    </div>
  ); 
}

export default SearchPage;