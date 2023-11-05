import { useState } from "react";

export function Counter1({ val = 0 }: any) {
  // let counterValue = val;
  //      getter        setter
  const [counterValue, setCounterValue] = useState(val); // react Hook

  function Increase(multiplayer: number) {
    setCounterValue(counterValue + multiplayer);
    console.log(counterValue);
  }

  return (
    <div>
      {counterValue}
      <button
        onClick={function Click() {
          Increase(3);
        }}
      >
        increase
      </button>
      <button onClick={() => Increase(3)}>increase</button>
      <button onClick={() => setCounterValue(counterValue - 6)}>
        decrease
      </button>
    </div>
  );
}

export function Input1({ val = "" }: any) {
  // 1.useState
  // 2.onChange,onClick=setCounterValue
  // 3.(input)value={counterValue}

  const [counterValue, setCounterValue] = useState(val);

  return (
    <div>
      {counterValue}
      <hr />
      <input
        type="text"
        onChange={(event) => setCounterValue(event.target.value)}
        value={counterValue}
      />
      <button
        className={counterValue == "" ? "пусто" : "не пусто"}
        onClick={() => setCounterValue("")}
      >
        null
      </button>
    </div>
  );
}

export function Li2({ val = 0, callbackFunc }: any) {
  return (
    <div onClick={() => callbackFunc(val * 10)}>
      <hr />
      {val * 2}
    </div>
  );
}

export function Ul2({ count = 0 }: any) {
  function PrintData(text: string) {
    console.log(text);
  }
  return (
    <div>
      {[1, 2, 3].map((item: number, index: number) => (
        <Li2 key={index} val={item} callbackFunc={PrintData} />
      ))}
    </div>
  );
}
