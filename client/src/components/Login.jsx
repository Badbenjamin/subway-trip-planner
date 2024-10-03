import { useState } from "react"

function Login() {
    const [username, setUserName] = useState('')
    const [password, setPassword] = useState('')

    
    function handleSubmit(e){
        e.preventDefault()
        const data ={
            'username' : username,
            'password' : password
        }
        fetch('http://127.0.0.1:5555/api/login', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            credentials: 'include',
            body : JSON.stringify(data),
        }).then((response) => {
            if (response.ok) {
                console.log("login succesful")
            } else {
                console.log('login failed')
            }
        });
    }

    return (
        <div>
            <form className="login-form" onSubmit={handleSubmit}>
                <label htmlFor="username">RiderName</label><br/>
                <input
                type="text"
                id="RiderName"
                value={username}
                onChange={(e) => setUserName(e.target.value)}
                /><br/>
                <label htmlFor="password">Password</label><br/>
                <input
                type="password"
                id="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                /><br/>
                <input type="submit" value='LOGIN'/>
            </form>
            <button>SIGN UP</button>
        </div>
       
    )
}

export default Login