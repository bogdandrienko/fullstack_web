import { useDispatch, useSelector } from "react-redux";

export function reducerSimpleReduxCounter(
  state = {},
  action: { type: string; payload: any }
) {
  switch (action.type) {
    case "negative":
      return { data: -1 * action.payload };
    case "positive":
      return { data: action.payload };
    default:
      return state;
  }
}

export default function Page() {
  const dispatch = useDispatch();
  const simpleReduxCounter = useSelector(
    (state: any) => state.simpleReduxCounter
  );
  return (
    <div>
      <h1>SimpleReduxCounterPage</h1>
      <div>
        {simpleReduxCounter.data ? simpleReduxCounter.data : "нет данных"}
      </div>
      <button
        onClick={() => {
          dispatch({ type: "negative", payload: 200 });
        }}
      >
        negative
      </button>
      <button
        onClick={() => {
          dispatch({ type: "positive", payload: 300 });
        }}
      >
        positive
      </button>
    </div>
  );
}
