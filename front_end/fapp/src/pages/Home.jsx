import React from "react";
import Searchcard from "../components/Searchcard";
import Footer from "../components/Footer";
import Navbar from "../components/Navbar";

import "../styles/Home.css"

function Home() {
    return (
        <div className="Home">
        <Navbar />
        <div className="container">
            <Searchcard />
            <article>
            <h1>HBRE </h1><p>Welcome to HBRE, your ultimate destination for all things real estate! 
            Whether you're buying, selling, renting, or investing, our platform is designed to provide you with 
            a seamless and comprehensive real estate experience.Just type in the location you want your real estate
            and we will do the hard job for you to find your dream home.</p>
            </article>
        </div>
        <Footer />
        </div>
    ); 
}

export default Home;