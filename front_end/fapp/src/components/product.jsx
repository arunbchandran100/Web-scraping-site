export function Product(props) {
    return (

        <div className='productList'>
            <div key={props.id} className='productCard'>
                <img src={props.image} alt='product-img' className='productImage'></img>

                

                <div className='productCard__content'>
                    <h3 className='productName'>{props.name}</h3>
                    <div className='displayStack__1'>
                        <div className='productPrice'>{props.price} Lacs</div>
                        <div className='productSales'>{props.totalSales} </div>
                    </div>
                    <div className='displayStack__2'>
                        {/* <div className='productRating'>
                            {[...Array(props.rating)].map((index) => (
                                <FaStar id={index + 1 } key={index} />
                            ))}
                        </div> */}
                        <div className='productTime'>{props.timeLeft} sq feet</div>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default Product;