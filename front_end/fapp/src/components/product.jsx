<<<<<<< Updated upstream
import { useState, useEffect } from "react";
import "../styles/product.css";
import { useNavigate } from "react-router-dom";

export function Products(props) {
  const [productData, setProductData] = useState([]);
  const [isLoading, setIsLoading] = useState(true); // Loading state

  // Update these as needed
  const city = 'New York';
  const locality = 'Manhattan';

  useEffect(() => {
    fetch(`http://localhost:8000/product/`)
      .then(response => response.json())
      .then(data => {
        setProductData(data);
        setIsLoading(false); // Set isLoading to false once data is fetched
      });
  }, [city, locality]);

  console.log(productData);

  const navigate = useNavigate();

  const handleMoreDetailsClick = (link) => {
    window.open(link, '_blank');
  };

  return (
    <div className='productList'>
      {isLoading ? ( // Render the loading page if isLoading is true
        <div className="loading">Loading...</div>
      ) : (
        productData.map((product, index) => (
          <div key={index} className='productCard'>
            <img src={product.image_urls[0]} alt={product.title} className='productImage' />
            <div className='productCard__content'>
              <h3 className='productName'>{product.title}</h3>
              <p className='productPrice'>Price: {product.price}</p>
              <p className='productLocation'>Location: {product.location}</p>
              <p className='productSquareFootage'>Square Footage: {product.square_footage}</p>
              <button className='productMoreDetailsButton' onClick={() => handleMoreDetailsClick(product.more_details_link)}>More Details</button>
            </div>
          </div>
        ))
      )}
    </div>
  );
}

=======
import React from 'react';
import '../styles/product.css';

export function Products(props) {
  // Temporary data
  const productData = [
    {
      id: 1,
      name: 'Product 1',
      price: 100,
      totalSales: 10,
      timeLeft: '200 sq feet',
      image: 'https://newprojects.99acres.com/projects/nest_makers/nest_bliss_in_the_woods/images/tsx2kcne_med.jpg',
      link: 'https://www.99acres.com/search/property/buy/hyderabad-all?city=38&preference=S&area_unit=1&res_com=R'
    },
    {
      id: 2,
      name: 'Product 2',
      price: 200,
      totalSales: 20,
      timeLeft: '300 sq feet',
      image: 'https://mediacdn.99acres.com/media1/20873/10/417470874M-1681280825224.jpg',
      link: 'https://www.99acres.com/search/property/buy/hyderabad-all?city=38&preference=S&area_unit=1&res_com=R'
    },
    {
      id: 2,
      name: 'Product 2',
      price: 200,
      totalSales: 20,
      timeLeft: '300 sq feet',
      image: 'https://mediacdn.99acres.com/media1/20873/10/417470874M-1681280825224.jpg',
      link: 'https://www.99acres.com/search/property/buy/hyderabad-all?city=38&preference=S&area_unit=1&res_com=R'
    },
    {
      id: 2,
      name: 'Product 2',
      price: 200,
      totalSales: 20,
      timeLeft: '300 sq feet',
      image: 'https://mediacdn.99acres.com/media1/20873/10/417470874M-1681280825224.jpg',
      link: 'https://www.99acres.com/search/property/buy/hyderabad-all?city=38&preference=S&area_unit=1&res_com=R'
    },
    {
      id: 2,
      name: 'Product 2',
      price: 200,
      totalSales: 20,
      timeLeft: '300 sq feet',
      image: 'https://mediacdn.99acres.com/media1/20873/10/417470874M-1681280825224.jpg',
      link: 'https://www.99acres.com/search/property/buy/hyderabad-all?city=38&preference=S&area_unit=1&res_com=R'
    },
    {
      id: 2,
      name: 'Product 2',
      price: 200,
      totalSales: 20,
      timeLeft: '300 sq feet',
      image: 'https://mediacdn.99acres.com/media1/20873/10/417470874M-1681280825224.jpg',
      link: 'https://www.99acres.com/search/property/buy/hyderabad-all?city=38&preference=S&area_unit=1&res_com=R'
    },
  ];

  const handleCardClick = (link) => {
    window.open(link, '_blank'); // Open the provided link in a new tab
  };

  return (
    <div className='productList'>
      {productData.map((product) => (
        <div key={product.id} className='productCard' onClick={() => handleCardClick(product.link)}>
          <img src={product.image} alt='product-img' className='productImage' />

          <div className='productCard__content'>
            <h3 className='productName'>{product.name}</h3>
            <div className='displayStack__1'>
              <div className='productPrice'>{product.price} Lacs</div>
              <div className='productSales'>{product.totalSales}</div>
            </div>
            <div className='displayStack__2'>
              <div className='productTime'>{product.timeLeft}</div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

>>>>>>> Stashed changes
export default Products;
