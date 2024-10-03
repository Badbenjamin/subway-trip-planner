import { useOutletContext, useNavigate } from "react-router-dom"

function Profile(){
    const {user, setUser} = useOutletContext()
    
    function handleClick(){
        fetch('/api/logout', {method: "DELETE"}).then((r) => {
            if (r.ok) {
                setUser(null)
                // why isnt this working?
                navegate('/')
            }
        })
    }

    if (!user) {
        return(
            <>no user</>
        )
    }
    return(
        <div>
            <h2>{user.username}</h2>
            <>Home Station: {user.my_stop.stop_name}</>
            <br/>
            <>Favorite Subway Activity: {user.fav_subway_activity}</>
            <br/>
            <button onClick={handleClick}>LOGOUT</button><button>EDIT PROFILE</button>
        </div>
    )
}

export default Profile