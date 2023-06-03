import React from "react";
import Navbar from "./components/Navbar";
import Searchcard from "./components/Searchcard";
import Footer from "./components/Footer";
import "./App.css";


function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="container">
        <Searchcard />
        <article>
          <h1>Website </h1>A website (also written as a web site) is a
          collection of web pages and related content that is identified by a
          common domain name and published on at least one web server. Websites
          are typically dedicated to a particular topic or purpose, such as
          news, education, commerce, entertainment or social networking.
        </article>
      </div>
      <Footer />
    </div>
  );
}

export default App;
