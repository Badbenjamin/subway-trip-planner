import { useState, useEffect } from 'react'
import { Outlet } from 'react-router-dom'
import '../App.css'

// import Home from './Home'
import Header from './Header'
import NavBar from './NavBar'
// import { Outlet } from "react-router-dom";

function App() {
  const [user, setUser] = useState(null)

  useEffect(() => {
    fetch('/api/check_session')
    .then((response) => {
      if (response.ok) {
        // console.log(response.user)
        response.json().then((user) => setUser(user));
      } else {
        console.log('user is not logged in')
      }
    });
  }, [])

  console.log(user)

    return (
      <>
        <NavBar user={user}/>
        <Header />
        <Outlet />
      </>
    )
}

export default App
