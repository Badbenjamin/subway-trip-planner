import Station from "./Station"
import { useOutletContext } from "react-router-dom";

function StopSearch({ props }) {

    const { stations } = useOutletContext()

    console.log(stations)
    const stationComponents = stations.map(station => {
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
            />
        </div>
    )
}

export default StopSearch