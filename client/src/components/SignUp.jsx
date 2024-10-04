import { useState, useEffect } from "react"
import Select from "react-select"
import { useNavigate } from "react-router-dom"

function SignUp(){
    const [username, setUserName] = useState('')
    const [password, setPassword] =useState('')
    const [favActivity, setFavActivity] = useState('')
    const [myStop, setMyStop] = useState(null)
    const [stations, setStations] = useState([])
    const navegate = useNavigate()
    // const [selectedOption, setSelectedOption] = useState(null)

    
    function handleSubmit(e){
        e.preventDefault()
        // console.log(myStop.value.id)
        const new_rider = {
            "username" : username,
            "password" : password,
            "fav_activity": favActivity,
            "my_stop_id" : myStop.value.id
        } 
        if (username.length < 1){
            alert("please enter a RiderName");
            return
        } 
        if (password.length <= 5){
            alert("please enter a password that is 5 characters or more")
            return
        }
        fetch('/api/signup', {
            method: 'POST',
            headers: {
                'Content-type' : 'application/json'
            },
            body: JSON.stringify(new_rider)
        })
        .then((response) => response.json())
        .then((data) => console.log(data))
        navegate('/profile');
        


       
    //   console.log(new_rider)
    }

    function showPw(){
        console.log('clicked')
    }

    useEffect(() => {
        fetch("http://127.0.0.1:5555/api/stations")
        .then((r) => r.json())
        .then((stationData) =>  setStations(stationData))
    }, [])

    // console.log(stations)

    const optionsArray = []

    for (const station of stations){
        const stationObj = { value : station, label: `${station.stop_name+" "+station.daytime_routes}`};
        optionsArray.push(stationObj);
    }

    const handleChange = (option) => {
        // setSelectedOption(option);
        setMyStop(option);
    }

    // console.log(optionsArray)

    const customStyles = {
        control : (provided) => ({
            ...provided,
            backgroundColor: 'white',
            fontWeight: 'bold',
            
        }),
        option: (provided, state) => ({
            ...provided,
            color: 'black',
            backgroundColor: state.isSelected ? 'lightblue' : 'white',
        }),
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
                <label htmlFor="my-stop">My Stop</label>
                    <Select
                        styles={customStyles}
                        value={myStop}
                        onChange={handleChange}
                        options={optionsArray}
                    />
                    <input type="submit" value='CREATE PROFILE'/>
            </form>
        </div>
    )
}

export default SignUp