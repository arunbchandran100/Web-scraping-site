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

export default Products;
