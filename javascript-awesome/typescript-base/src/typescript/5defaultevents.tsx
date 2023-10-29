import React from "react";

export default function Ex() {
  function formSubmitHandler(event: React.FormEvent) {
    // event.target
    // event.preventDefault();
  }

  function buttonClickHandler(event: React.MouseEvent<HTMLButtonElement>) {
    // event.preventDefault();
    // event.bind()
  }

  function inputChangeHandler(event: React.ChangeEvent<HTMLInputElement>) {
    // event.target
    // event.target.value
  }

  function dragHandler(event: React.DragEvent<HTMLDivElement>) {
    // event.target
    // event.target.value
  }

  return (
    <div>
      typescript
      <form onSubmit={formSubmitHandler}>
        <button type={"submit"}>getData</button>
      </form>
      <button onClick={buttonClickHandler}>getData</button>
      <input type={"text"} onChange={inputChangeHandler}>
        getData
      </input>
      <div onDrag={dragHandler}>DRAG ME</div>
    </div>
  );
}
