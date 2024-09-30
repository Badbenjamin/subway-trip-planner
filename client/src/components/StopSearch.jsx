import Station from "./Station"
import { useOutletContext } from "react-router-dom";
import { useState } from "react";

function StopSearch({ props }) {

    const { stations } = useOutletContext();
    const [searchText, setSearchText] = useState('');

    function onChange(e){
        setSearchText(e.target.value);
    }

    const filteredStations = stations.filter(station => {
        return station.stop_name.toUpperCase().includes(searchText.toUpperCase())
    })
    console.log(filteredStations)

    // console.log(stations)
    const stationComponents = filteredStations.map(station => {
        return <Station key={station.id} station={station} />
    })



    return (
        <div className="searchBar">
            <label htmlFor="search"></label>
            <input
                name="q"
                type="text"
                id="search"
                placeholder="Pick a station..."
                onChange={onChange}
                value={searchText}
            />
            <ul>{stationComponents}</ul>
        </div>
    )
}

export default StopSearch