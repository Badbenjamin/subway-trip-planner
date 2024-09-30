
function Station({ station, getStations, position }) {

    // console.log(station)

    function handleClick(){
        getStations(station, position)
    }
    
    return (
        <button station={station} onClick={handleClick}>{station.stop_name+" "+station.daytime_routes}</button>
    )
}

export default Station