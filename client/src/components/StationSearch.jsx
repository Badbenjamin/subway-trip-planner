import Station from "./Station"
import { useOutletContext } from "react-router-dom";
import { useState } from "react";

function StationSearch({getStations, position}) {

    const { stations } = useOutletContext();
    const [searchText, setSearchText] = useState('');

    function onChange(e){
        setSearchText(e.target.value);
    }


    function onClick(e){
        console.log(e.target)
    }
    


    const filteredStations = stations.filter(station => {
        return station.stop_name.toUpperCase().includes(searchText.toUpperCase())
    })
    // console.log(filteredStations)

    // console.log(stations)
    const stationListItem = filteredStations.map(station => {
        return <Station getStations={getStations} onClick={onClick} key={station.id} station={station} position={position}/>
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
            <ul>{stationListItem}</ul>
        </div>
    )
}

export default StationSearch