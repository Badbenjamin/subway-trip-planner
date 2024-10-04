import { useState } from "react"

function SignUp(){
    const [username, setUserName] = useState('')
    const [password, setPassword] =useState('')
    const [favActivity, setFavActivity] = useState('')
    const [myStop, setMyStop] = useState(null)

    function handleSubmit(e){
        e.preventDefault()
        console.log('signup')
    }

    function showPw(){
        console.log('clicked')
    }

    return(
        <div>
            <h2>CREATE PROFILE</h2>
            <form className="signup-form" onSubmit={handleSubmit}>
                <label htmlFor="username">RiderName</label><br/>
                    <input
                    type="text"
                    id="RiderName"
                    value={username}
                    onChange={(e) => setUserName(e.target.value)}
                    />
                <br/>
                    <label htmlFor="password">Password</label><br/>
                    <input
                    type="password"
                    id="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    />
                    {/* <label for="check">Show Password</label>
                        <input id="check" type="checkbox" onClick={showPw}>show password</input> */}
                <br/>
                    <label htmlFor="password">Favorite Subway Activity</label><br/>
                    <input
                    type="text"
                    id="Activity"
                    value={favActivity}
                    onChange={(e) => setFavActivity(e.target.value)}
                    />
                <br/>
                    <input type="submit" value='CREATE PROFILE'/>
            </form>
        </div>
    )
}

export default SignUp