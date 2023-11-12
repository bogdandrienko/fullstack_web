import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as constants from "../components/constants";
import * as actions from "../components/actions";
import * as loaders from "../components/ui/loaders";
import * as modals from "../components/ui/modals";
import { Link } from "react-router-dom";

export default function Page() {
  const dispatch = useDispatch();
  const storeTodoList = useSelector((state: any) => state.storeTodoList);
  useEffect(() => {
    if (constants.DEBUG) {
      console.log(storeTodoList);
    }
  }, [storeTodoList]);

  useEffect(() => {
    if (!storeTodoList.data) {
      actions.getTodoList(dispatch, "?search=Все");
    }

    setTimeout(() => {
      console.log("setTimeout"); // просто выполнить действие после задержки один раз
    }, 1000);

    setInterval(() => {
      console.log("setInterval"); // просто выполнять действие после задержки бесконечно(его можно остановить)
    }, 60000);

    Delay(() => {
      console.log("Delay");
    }, 1000);
    Delay(() => {
      console.log("Delay");
    }, 2000);
    Delay(() => {
      console.log("Delay");
    }, 3000);
  }, []);

  function Delay(callback: any, timeout: number) {
    setTimeout(() => {
      callback();
    }, timeout);
  }

  return (
    <div>
      TodoListReduxPage
      <button
        onClick={() => {
          actions.getTodoList(dispatch, "?search=Все&filter=today");
        }}
      >
        getTodoList
      </button>
      <hr />
      <hr />
      <hr />
      {storeTodoList.load && <loaders.Loader1 />}
      {storeTodoList.fail && (
        <modals.Fail1>Обратитесь к администратору</modals.Fail1>
      )}
      {storeTodoList.error && (
        <modals.Error1>{storeTodoList.error}</modals.Error1>
      )}
      <hr />
      {storeTodoList.data && storeTodoList.data.length > 0 ? (
        <ul>
          {storeTodoList.data.map((item: any, index: number) => (
            <li key={item.id}>
              <Link to={`/todos/${item.id}`}>
                #{index + 1}
                {item.title}({item.id})
              </Link>
            </li>
          ))}
        </ul>
      ) : (
        <div>Данных нет!</div>
      )}
      <hr />
      {storeTodoList.data && storeTodoList.data.length > 0 ? (
        <table>
          <tbody>
            {storeTodoList.data.map((item: any, index: number) => (
              <tr key={item.id}>
                <td>#{index + 1}</td>
                <td>{item.title}</td>
                <td>{item.description}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <div>Данных нет!</div>
      )}
      <hr />
    </div>
  );
}
