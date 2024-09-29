import Station from "./Station"
import { useOutletContext } from "react-router-dom";

function StationList({ props }) {

    const { stations } = useOutletContext()

    console.log(stations)
    const stationComponents = stations.map(station => {
        return <Station key={station.id} station={station} />
    })



    return (
        <ul>{stationComponents}</ul>
    )
}

export default StationList