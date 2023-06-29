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
            <h1>Online Property Scanner </h1><p>Welcome to our Online Property Scanner! Whether you are looking to buy 
                a property or explore real estate options, our website is here to make your search 
                process easier. With our advanced search feature, you can find properties for sale 
                in your desired city and locality. Simply enter the city and locality information, 
                and our website will search through multiple reliable sources to provide you with 
                comprehensive results. We understand that finding the perfect property can be a 
                daunting task, but with our platform, you can save time and effort by accessing all 
                the relevant listings in one place. Start your property search today and discover the
                 home of your dreams!

At our Online Property Scanner, we aim to simplify the process of finding properties for sale and exploring real estate options. We have partnered with leading property listing websites to aggregate data from various sources, ensuring that you have access to a wide range of listings. When you enter your desired city and locality, our website utilizes powerful search algorithms to fetch the latest property information from multiple websites. You can easily browse through the search results, filter properties based on your preferences, and view detailed property descriptions, photos, and contact information. We are committed to providing a seamless and efficient property search experience, empowering you to make informed decisions about buying real estate. Start your search today and find your perfect property match!</p>
            </article>
        </div>
        <Footer />
        </div>
    ); 
}

export default Home;