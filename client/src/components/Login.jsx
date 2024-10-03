
function Login() {


    return (
        <div>
            <form >
                <label htmlFor="username">RiderName</label>
                <input
                type="text"
                id="RiderName"
                />
                <label htmlFor="username">Password</label>
                <input
                type="password"
                id="Password"
                />
            </form>
            <button>LOGIN</button>
            <button>SIGN UP</button>
        </div>
       
    )
}

export default Login