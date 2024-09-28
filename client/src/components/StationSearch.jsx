import { useState, useEffect } from "react";
// import { useOutletContext } from "react-router-dom";
import StationList from "./StationList";


function StationSearch({ props }) {

    // const { stations } = useOutletContext()

    console.log(props)

    return (
        <>
            <h1>this is the station search</h1>
            <StationList props={props} />
        </>

    )
}

export default StationSearch