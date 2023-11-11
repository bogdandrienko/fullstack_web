import React, { useEffect, useState } from "react";

export default function Page() {
  let counterBug = 666;
  //         getter(let)  setter(func)
  const [counter, setCounter] = useState(666); //
  function increase() {
    setCounter(counter + 1); // условно async
    counterBug = counterBug + 1;
    console.log(counterBug);
  }
  function decrease() {
    setCounter(counter - 1); // условно async
    counterBug = counterBug - 1;
    console.log(counterBug);
  }

  useEffect(() => {
    console.log("useState counter: " + counter);
  }, [counter]);

  return (
    <div>
      <h1>SimpleCounterPage</h1>
      <div>
        <h2>{counterBug}</h2>
        <h2>{counter}</h2>
        <button onClick={increase}>increase</button>
        <button onClick={decrease}>decrease</button>
      </div>
    </div>
  );
}
