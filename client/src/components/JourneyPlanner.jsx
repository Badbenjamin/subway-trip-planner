import { useState, useEffect } from "react";
// import { useOutletContext } from "react-router-dom";
import './Component.css'
import StationSearch from "./StationSearch";
import TripInfo from "./TripInfo";



function JourneyPlanner() {

    // const { stations } = useOutletContext()
    const [journeyStations, setJourneyStations] = useState([null, null])
    const [tripInfo, setTripInfo] = useState([])

    // console.log(journeyStations)
  
    function getStations(station, position){
        console.log(station.pos.position)
        const journey = [...journeyStations]
        if (station.pos.position === 'start'){
            journey[0] = station.value;
        } else if (station.pos.position == 'end'){
            journey[1] = station.value;
        }
        
    setJourneyStations(journey)
    }

    function planTrip(e){
        
        if (journeyStations[0] == null || journeyStations[1] == null){
            console.log('enter start and end stations')
        } else{
            fetch(`http://127.0.0.1:5555/api/plan_trip/${journeyStations[0].gtfs_stop_id}/${journeyStations[1].gtfs_stop_id}`)
            .then(response => response.json())
            .then(stopData => setTripInfo(stopData))
        }
    }

    // console.log(tripInfo)

    return (
        <div>
            {tripInfo[0] !== undefined ? <TripInfo tripInfo={tripInfo}/> : ""}
            <br></br>
            <div className='journey-planner'>
                <h2>Start Station</h2>
                <StationSearch getStations={getStations} position={"start"}/>
                <h2>End Station</h2>
                <StationSearch getStations={getStations} position={"end"}/>
                <br></br>
                <button onClick={planTrip}>Plan Trip</button>
            </div>
        </div>

    )
}

export default JourneyPlanner