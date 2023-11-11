import React, { useState } from "react";

export default function Page() {
  //         getter(let)  setter(func)
  const [counter, setCounter] = useState(666); //
  function increase() {
    setCounter(counter + 1);
  }

  function decrease() {
    setCounter(counter - 1);
  }

  return (
    <div>
      <h1>SimpleCounterPage</h1>
      <div>
        <h2>{counter}</h2>
        <button onClick={increase}>increase</button>
        <button onClick={decrease}>decrease</button>
      </div>
    </div>
  );
}
