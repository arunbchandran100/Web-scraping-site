// export function Product(props) {
//     return (

//         <div className='productList'>
//             <div key={props.id} className='productCard'>
//                 <img src={props.image} alt='product-img' className='productImage'></img>

                

//                 <div className='productCard__content'>
//   <img src="https://images.nobroker.in/images/8a9fd8828760f801018760ffd9f8018c/8a9fd8828760f801018760ffd9f8018c_60330_508297_thumbnail.jpg" alt="Product Image" />
//   <h3 className='productName'>2 BHK House  For Sale  In Oragadam Industrial Corridor</h3>
//   <div className='displayStack__1'>
//     <div className='productPrice'>42 Lacs</div>
//     <div className='productSales'>7479</div>
//   </div>
//   <div className='displayStack__2'>
//     {/* <div className='productRating'>
//         {[...Array(5)].map((_, index) => (
//             <FaStar id={index + 1} key={index} />
//         ))}
//     </div> */}
//     <div className='productTime'>1000 sq feet</div>
//   </div>
// </div>


//             </div>
//         </div>
//     )
// }
// export default Product;
import React from 'react';
import { FaBed, FaBath } from 'react-icons/fa'
import { RiApps2Fill } from 'react-icons/ri'
import "../styles/globals.css";


const Property = ({ item }) => {
    const { rooms, bath, isVerified, agency: { logo }, price, title, rentFrequency, area, externalID } = item;
//  let API = "";
//  const  fetchApiData = async(url) =>{
//     try{
//         const res = await fetch(url);
//         const data = await res.json();
//         console.log(data);
//     }
//     catch(error)
//     {
//         console.log(error);
//     }
//     };
//     useEffect(()=>
//     {
//         fetchApiData(API);
    
//     },[]);
 
    return (
        <Link href={`/property/${externalID}`} passHref>
            <Flex flexDirection="column" cursor="pointer">
                <Box>
                    <Image src={item.coverPhoto ? item.coverPhoto.url : item.coverPhoto} alt="bannerImage" width="450px" height="250px" />
                </Box>

                <Box mt={1}>
                    <Flex justifyContent="space-between" alignItems="center" >
                        <Flex flex alignItems="center" justifyContent="space-between" gap="0 5px">
                            {}
                            <Text fontSize="lg" fontWeight="bold">Rs {price}{rentFrequency ? `` : ""}</Text>
                        </Flex>
                        {}
                    </Flex>
                    <Flex alignItems="center" fontSize="16px" color="black.500" gap="0 15px">
                        {rooms} <FaBed /> 
                        | {bath} <FaBath /> | {millify(area)} sqft <RiApps2Fill />
                    </Flex>
                    <Box mt={4}>
                        <Text fontSize="lg">{title.length > 40 ? `${title.substring(0, 40)}...` : title}</Text>
                    </Box>
                </Box>
            </Flex>
        </Link>
    );
};

export default Property;