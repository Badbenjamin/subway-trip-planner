import { useState, useEffect } from 'react'
import { Outlet } from 'react-router-dom'
import '../App.css'

// import Home from './Home'
import Header from './Header'
import NavBar from './NavBar'
// import { Outlet } from "react-router-dom";

function App() {
  const [stations, setStations] = useState([])

  useEffect(() => {
    fetch("http://127.0.0.1:5555/api/stations")
      .then(response => response.json())
      .then(stationsData => setStations(stationsData))
  }, [])

  // console.log(stations)
  if (stations == []) {
    return <>loading...</>
  }

  if (stations != [])
    return (
      <>
        <NavBar />
        <Header />
        <Outlet context={{ stations: stations }} />
      </>
    )
}

export default App
