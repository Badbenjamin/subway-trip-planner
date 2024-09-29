import { useState, useEffect } from "react";
// import { useOutletContext } from "react-router-dom";
import StationList from "./StationList";



function StationSearch() {

    // const { stations } = useOutletContext()



    return (
        <>
            <h1>this is the station search</h1>
            <StationList />
        </>

    )
}

export default StationSearch