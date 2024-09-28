import { useState, useEffect } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import '../App.css'
import StationSearch from './StationSearch'
// import { Outlet } from "react-router-dom";

function App() {
  const [stations, setStations] = useState([])

  useEffect(() => {
    fetch("http://127.0.0.1:5555/api/stations")
      .then(response => response.json())
      .then(stationsData => setStations(stationsData))
  }, [])

  console.log(stations)
  if (stations == []) {
    return <>loading...</>
  }

  if (stations != [])
    return (
      <>
        <h1>SUBWAY TRIP PLANNER</h1>
        <StationSearch props={stations} />
      </>
    )
}

export default App
