import React from 'react';
import "../styles/Footer.css";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-column">
            <h3 className="footer-heading">Services</h3>
            <ul className="footer-links">
              <li><a href="#">Web design</a></li>
              <li><a href="#">Development</a></li>
              <li><a href="#">Hosting</a></li>
            </ul>
          </div>
          <div className="footer-column">
            <h3 className="footer-heading">About</h3>
            <ul className="footer-links">
              <li><a href="#">Company</a></li>
              <li><a href="#">Team</a></li>
              <li><a href="#">Legacy</a></li>
            </ul>
          </div>
          <div className="footer-column">
            <h3 className="footer-heading">Careers</h3>
            <ul className="footer-links">
              <li><a href="#">Job openings</a></li>
              <li><a href="#">Employee success</a></li>
              <li><a href="#">Benefits</a></li>
            </ul>
          </div>
          <div className="footer-column">
            <h3 className="footer-heading">Follow Us</h3>
            <ul className="social-icons">
              <li><a href="#"><i className="fab fa-facebook-f"></i></a></li>
              <li><a href="#"><i className="fab fa-twitter"></i></a></li>
              <li><a href="#"><i className="fab fa-instagram"></i></a></li>
              <li><a href="#"><i className="fab fa-linkedin"></i></a></li>
            </ul>
          </div>
        </div>
      </div>
      <div className="footer-bottom">
        <div className="container">
          <p className="footer-text">&copy; {new Date().getFullYear()} Website. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
