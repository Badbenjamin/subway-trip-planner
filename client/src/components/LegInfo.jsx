import './Component.css'


function LegInfo({tripInfo}){

        console.log(tripInfo)

    return(
        <div class="leg-info-grid-cointainer">
            <div class="start-station-info">
                <div class="top">{tripInfo[0].direction_label} Bound {tripInfo[0].route}</div>
                <div class="middle">{tripInfo[0].start_station_name}</div>
                <div class="bottom">Departs {tripInfo[0].start_station_arrival.slice(10,-3)}</div>
            </div>
            <div class="middle-info">
                <div class="top"># of stops</div>
                <div class="middle">→</div>
                <div class="bottom"></div>
            </div>
            <div class="end-station-info">
                <div class="top">{tripInfo[0].end_station_name}</div>
                <div class="middle">Arrives {tripInfo[0].end_station_arrival.slice(10,-3)}</div>
                <div class="bottom">transfer or destination</div>
            </div>
        </div>
    )
}

export default LegInfo