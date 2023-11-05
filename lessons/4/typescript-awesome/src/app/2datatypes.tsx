interface Action {
  // id: any; // bad
  id: number; // good
  name: string;
}

interface Group {
  id: number;
  name: string;
  actions: Action[];
}

interface User {
  id: number | string;
  name: string;
  email: string;
  groups: Group[]; // Group - one, Group[] - many
}

class Todo {
  constructor(param: {
    id: number;
    completed: boolean;
    title: string;
    userId: number;
  }) {
    return new Todo(param);
  }
}

export default function Ex() {
  let val1: string = "12";
  // @ts-ignore
  // val1 = 12
  // val1 = `12`

  const action: Action = { id: 1, name: "create" };
  const actions: Action[] = [
    { id: 1, name: "create" }, // , ids: 2
    // { id: 2, name: "create", new: true },
  ];

  const td2: Todo = new Todo({
    userId: 1,
    id: 1,
    title: "Hello",
    completed: true,
  });

  return <div>typescript</div>;
}
