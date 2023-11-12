import { useDispatch } from "react-redux";

export function ReducerAnotherReduxPage(
  state = {},
  action: { type: string; payload: any }
) {
  switch (action.type) {
    case "action1":
      return { data: "action1" };
    case "action2":
      return { data: "action2" };
    default:
      return state;
  }
}

export function Navbar1() {
  const dispatch = useDispatch();
  function ActionOne() {
    dispatch({ type: "action1" });
  }
  function ActionTwo() {
    dispatch({ type: "action2" });
  }
  return (
    <div>
      Navbar1
      <hr />
      <button onClick={ActionOne}>ActionOne</button>
      <hr />
      <button onClick={ActionTwo}>ActionTwo</button>
      <hr />
    </div>
  );
}
