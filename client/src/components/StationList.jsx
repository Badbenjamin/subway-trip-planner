import Station from "./Station"

function StationList({ props }) {

    // console.log(props)


    const stationComponents = props.map(station => {
        return <Station key={station.id} station={station} />
    })



    return (
        <ul>{stationComponents}</ul>
    )
}

export default StationList