import { NavLink } from "react-router-dom"

function NavBar({user}) {

    console.log(user)

    return (
        <nav className="navbar">
            <NavLink to="/" style={{ textDecoration: 'none' }}>HOME</NavLink>
            <>      </>
            <NavLink to="/login" style={{ textDecoration: 'none' }}>LOGIN</NavLink>
        </nav>
    )
}

export default NavBar