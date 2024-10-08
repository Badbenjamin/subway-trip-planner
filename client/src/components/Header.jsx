import TimeDate from "./TimeDate"
import { useState, useEffect } from "react"

function Header() {

    const [timeDate, setTimeDate] = useState(new Date())

    useEffect(()=>{

        let timer = setInterval(()=>setTimeDate(new Date()), 1000)

        return function clearnup() {
            clearInterval(timer)
        }
    });


    return (
        <div className="site-header">
            <h1>Subway Trip Planner</h1>
            <TimeDate/>
        </div>
        
    )
}

export default Header