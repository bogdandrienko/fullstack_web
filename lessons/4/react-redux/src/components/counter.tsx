import { useDispatch, useSelector } from "react-redux";

export function Counter1() {
  const dispatch = useDispatch(); // хук для переключений reducer-ов в state(store)
  return (
    <div>
      {true && "JSX"}
      <button
        onClick={() => {
          dispatch({ type: "negative", payload: 666 });
          // only write
        }}
      >
        negative
      </button>
      <button
        onClick={() => {
          dispatch({ type: "positive", payload: 777 });
          // only write
        }}
      >
        positive
      </button>
    </div>
  );
}
