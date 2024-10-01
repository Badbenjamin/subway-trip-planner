function TripInfo({tripInfo}){



    if (tripInfo == []){
        return(
            <>trip info here</>
        )
    }
    console.log(tripInfo[0])

    return(
        <div>
            <p>{tripInfo[0].start_station_name} {tripInfo[0].direction_label} Bound {tripInfo[0].route}: Arrival Time: {tripInfo[0].start_station_arrival}</p>
            <p>{tripInfo[0].end_station_name} : Arrival Time {tripInfo[0].end_station_arrival}</p>
            <p>Your Train left {tripInfo[0].last_station_name} at {tripInfo[0].last_station_departure}</p>
        </div>
        
    )
}

export default TripInfo