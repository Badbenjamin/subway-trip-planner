import { useState, useEffect } from "react";
// import { useOutletContext } from "react-router-dom";
import './Component.css'
import StopSearch from "./StopSearch";



function JourneyPlanner() {

    // const { stations } = useOutletContext()



    return (
        <>
            <h1>Journey Planner</h1>
            <div class='flexbox-container'>
                <h2>Start Station</h2>
                <StopSearch />
                <h2>End Station</h2>
                <StopSearch/>
            </div>
        </>

    )
}

export default JourneyPlanner