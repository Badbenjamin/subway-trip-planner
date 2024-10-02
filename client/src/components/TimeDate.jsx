import { useState, useEffect } from "react"
import './Component.css'

function TimeDate(){

    const [timeDate, setTimeDate] = useState(new Date())

    useEffect(()=>{

        let timer = setInterval(()=>setTimeDate(new Date()), 1000)

        return function clearnup() {
            clearInterval(timer)
        }
    });

    return(
        <h2>NYC {timeDate.toLocaleTimeString()}</h2>
    )
}

export default TimeDate