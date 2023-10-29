interface Action {
  id: number; // good
  // id: any; // bad
  name: string;
}
interface Group {
  id: number;
  name: string;
  actions: Action[];
}
interface User {
  id: number;
  name: string;
  email: string;
  groups: Group[];
}

class Todo {
  constructor(param: {
    id: number;
    completed: boolean;
    title: string;
    userId: number;
  }) {}
}

export default function Ex() {
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
