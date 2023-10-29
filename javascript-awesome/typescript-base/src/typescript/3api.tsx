import axios from "axios";

interface Todo {
  userId: number;
  id: number;
  title: string;
  completed: boolean;
}

export default function Ex() {
  async function getData(): Promise<Todo> {
    //     const response = await axios.get<Todo[]>(
    //   `https://jsonplaceholder.typicode.com/todos`,
    // );
    const { data } = await axios.get<Todo[]>(
      `https://jsonplaceholder.typicode.com/todos`,
    );
    // console.log(data.filter())
    console.log(data[2].title);
    return data[2];
  }

  async function sendData(todo: Todo): Promise<boolean> {
    const response = await axios.post(
      `https://jsonplaceholder.typicode.com/todos`,
      todo,
    );
    console.log(response);
    return true;
  }

  async function check() {
    const td1: Todo = await getData();
    const res: boolean = await sendData(td1);
  }

  check();

  return <div>typescript</div>;
}
