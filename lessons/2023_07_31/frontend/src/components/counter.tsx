import React, {useState} from 'react';

export function Counter1({counter} : {counter: number}): JSX.Element{
    return (<div>1111111{counter}</div>)
}

// @ts-ignore
export function Counter2(){

    //     getter            setter                                      hooks
    const [counter, setCounter] = useState(666)
    const [username, setUsername] = useState("Bogdan")

    // var
    // let counter2 = 12
    // const counter

    function Increase(){
        setCounter(counter*9)
    }

    function Decrease(){
        setCounter(counter-1)
    }

    return (<div>

        <input type={"text"} value={username} onChange={(event)=> {
            event.preventDefault();
            setUsername(event.target.value)
        }}/>
        <input type={"datetime-local"} value={username} onChange={(event)=> setUsername(event.target.value)}/>

        <button onClick={Increase}>Increase</button>
        {counter}
        <button onClick={Decrease}>Decrease</button>

        <div>{username}</div>
        <div>{username}</div>
        <div>{username}</div>
        <div>{username}</div>
        <div>{username}</div>
        <div>{username}</div>

    </div>)
}