import { NavLink } from "react-router-dom"
import './Component.css'

function NavBar() {
    return (
        <nav className="navbar">
            <NavLink to="/">HOME</NavLink>
            <>  </>
            <NavLink to="/login">LOGIN</NavLink>
        </nav>
    )
}

export default NavBar