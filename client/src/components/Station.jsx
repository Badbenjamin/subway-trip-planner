
function Station({ station }) {

    // console.log(station)

    return (
        <div>{station.stop_name+" "+station.daytime_routes}</div>
    )
}

export default Station