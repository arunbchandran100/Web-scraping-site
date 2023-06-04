import React, { useRef } from "react";
import Card from "react-bootstrap/Card";
import "../styles/Searchcard.css";

function Card2() {
  return (
    <div className="rechargephoto">
      <Card className="rechargephoto-card" /*onClick={handleClick}*/>
        <Card.Img
          variant="top"
          src="https://media.istockphoto.com/id/1322277517/photo/wild-grass-in-the-mountains-at-sunset.jpg?s=612x612&w=0&k=20&c=6mItwwFFGqKNKEAzv0mv6TaxhLN3zSE43bWmFN--J5w="
        />
      </Card>

      <Card className="rechargephoto-card" /*onClick={handleClick}*/>
        <Card.Img
          variant="top"
          src="https://media.istockphoto.com/id/1322277517/photo/wild-grass-in-the-mountains-at-sunset.jpg?s=612x612&w=0&k=20&c=6mItwwFFGqKNKEAzv0mv6TaxhLN3zSE43bWmFN--J5w="
        />
      </Card>
    </div>
  );
}

export default Card2;
