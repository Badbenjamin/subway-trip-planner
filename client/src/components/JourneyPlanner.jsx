import { useState, useEffect } from "react";
// import { useOutletContext } from "react-router-dom";
import './Component.css'
import StationSearch from "./StationSearch";
import TripInfo from "./TripInfo";



function JourneyPlanner() {

    // const { stations } = useOutletContext()
    const [journeyStations, setJourneyStations] = useState([null, null])
    const [tripInfo, setTripInfo] = useState([])

    
  
    function getStations(station, position){
        const journey = [...journeyStations]
        if (position === 'start'){
            journey[0] = station;
        } else if (position == 'end'){
            journey[1] = station;
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
            <TripInfo tripInfo={tripInfo}/>
            <div>
                <button onClick={planTrip}>Plan Trip</button>
            </div>
            <div className='flexbox-container'>
                <h2>Start Station: {journeyStations[0] === null ? "" : journeyStations[0].stop_name}</h2>
                <StationSearch getStations={getStations} position={"start"}/>
                <h2>End Station: {journeyStations[1] === null ? "" : journeyStations[1].stop_name}</h2>
                <StationSearch getStations={getStations} position={"end"}/>
            </div>
        </div>

    )
}

export default JourneyPlanner