import React from "react";
import Navbar from "./components/Navbar";
import Searchcard from "./components/Searchcard";
import Footer from "./components/Footer";
import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import SearchPage from "./pages/SearchPage";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/search" element={<SearchPage />} />
      </Routes>
    </BrowserRouter>
  ); 
}

export default App;