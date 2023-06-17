export function Product(props) {
    return (

        <div className='productList'>
            <div key={props.id} className='productCard'>
                <img src={props.image} alt='product-img' className='productImage'></img>

                

                <div className='productCard__content'>
  <img src="https://images.nobroker.in/images/8a9fd8828760f801018760ffd9f8018c/8a9fd8828760f801018760ffd9f8018c_60330_508297_thumbnail.jpg" alt="Product Image" />
  <h3 className='productName'>2 BHK House  For Sale  In Oragadam Industrial Corridor</h3>
  <div className='displayStack__1'>
    <div className='productPrice'>42 Lacs</div>
    <div className='productSales'>7479</div>
  </div>
  <div className='displayStack__2'>
    {/* <div className='productRating'>
        {[...Array(5)].map((_, index) => (
            <FaStar id={index + 1} key={index} />
        ))}
    </div> */}
    <div className='productTime'>1000 sq feet</div>
  </div>
</div>


            </div>
        </div>
    )
}
export default Product;