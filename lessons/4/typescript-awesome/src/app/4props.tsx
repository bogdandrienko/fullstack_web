import axios from "axios";
import { useState } from "react";

interface Todo {
  userId: number;
  id: number;
  title: string;
  completed: boolean;
}

function TodoComponent(props: Todo) {
  return (
    <div>
      <hr />
      <h1 className="">
        {props.title} [{props.userId}]
      </h1>
      <div className="">{props.completed ? "готово" : "не готово"}</div>
      <br />
    </div>
  );
}

export default function Ex() {
  const [todos, setTodos] = useState<Todo[]>([]);
  async function getData(): Promise<Todo[]> {
    const { data } = await axios.get<Todo[]>(
      "https://jsonplaceholder.typicode.com/todos",
    );
    console.log(data);
    return data;
  }

  async function getTodos() {
    const data: Todo[] = await getData();
    setTodos(data);
  }

  return (
    <div>
      typescript
      <button onClick={getTodos}>getData</button>
      <ul>
        {todos.length > 1
          ? todos.map((todo, index) => (
              <TodoComponent key={todo.id} {...todo} />
            ))
          : "no data"}
      </ul>
    </div>
  );
}
