import { useDispatch, useSelector } from "react-redux";

import { Counter1 } from "../components/counter";

export function reducerSimpleReduxCounter(
  state = { data: 0 },
  action: { type: string; payload: any }
) {
  switch (action.type) {
    case "negative1":
      return { data: action.payload - 1 };
    case "positive":
      return { data: action.payload + 1 };
    case "null":
      return { data: undefined };
    case "error":
      return { error: "error 2", data: undefined };
    default:
      return state;
  }
}

export default function Page() {
  const simpleReduxCounter = useSelector(
    (state: any) => state.simpleReduxCounter
  ); // useSelector - берёт переменную из combineReducers
  // only read
  return (
    <div>
      <h1>SimpleReduxCounterPage</h1>
      <div>{simpleReduxCounter.data}</div>
      <Counter1 />
    </div>
  );
}
