import axios from "axios";

export function Api1() {
  function GetData1() {
    // full production: service.tsx (....)

    // устарел
    axios
      .get("https://jsonplaceholder.typicode.com/todos")
      .then((r) => {
        // 200 | 201 ... ~200
        console.log(r);
      })
      .catch((err) => {
        console.error(`err: ${err}`);
        // модальное окно
      })
      .finally(() => {
        console.log("finally");
      });
  }

  async function GetData2() {
    try {
      const data = { name: "Danat" };
      // const response = await axios.post("", data)
      // Headers, Authorization, Tokens...

      const response = await axios.get(
        `https://jsonplaceholder.typicode1.com/todos`,
      );
      console.log(response);
    } catch (err) {
      console.error(err);
    }
  }

  const data = undefined;

  return (
    <div>
      <hr />
      <button onClick={GetData2}>GetData</button>
      {data === undefined ? "no data" : "data"}
    </div>
  );
}

// initial
// load (крутить спинер, не отрисовывать данные)
// success (остановить лоадер, не отрисовывать данные)
// fail[frontend] (остановить лоадер, не отрисовывать данные, но нужно модальное окно)
// error[backend] (остановить лоадер, не отрисовывать данные, но нужно модальное окно)
// reset (=> logout)
// ...
