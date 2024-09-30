import { useState, useEffect } from "react";
// import { useOutletContext } from "react-router-dom";
import './Component.css'
import StationSearch from "./StationSearch";



function JourneyPlanner() {

    // const { stations } = useOutletContext()
    const [journeyStations, setJourneyStations] = useState([null, null])

    
  
    function getStations(station, position){
        const journey = [...journeyStations]
        if (position === 'start'){
            journey[0] = station;
        } else if (position == 'end'){
            journey[1] = station;
        }
        
    setJourneyStations(journey)
    }
   
    console.log(journeyStations)

    return (
        <>
            <h1>Journey Planner</h1>
            <div className='flexbox-container'>
                <h2>Start Station </h2>
                <StationSearch getStations={getStations} position={"start"}/>
                <h2>End Station </h2>
                <StationSearch getStations={getStations} position={"end"}/>
            </div>
        </>

    )
}

export default JourneyPlanner