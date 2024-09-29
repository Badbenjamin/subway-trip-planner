import { useState, useEffect } from "react";
// import { useOutletContext } from "react-router-dom";
import StopSearch from "./StopSearch";



function JourneyPlanner() {

    // const { stations } = useOutletContext()



    return (
        <>
            <h1>Journey Planner</h1>
            <h2>Start Station</h2>
            <StopSearch />
            <h2>End Station</h2>
            <StopSearch />
        </>

    )
}

export default JourneyPlanner