import axios from "axios";
import {
  errorWeb,
  failWeb,
  loadWeb,
  successWeb,
} from "../pages/SimpleReduxWebPage";
import * as constants from "../components/constants";

export async function getData(dispatch: any) {
  try {
    dispatch({ type: loadWeb });
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com1/todos"
    );
    setTimeout(() => {
      if (response.status === 200 || response.status === 201) {
        dispatch({ type: successWeb, payload: response.data });
      } else {
        dispatch({ type: errorWeb, payload: response.statusText });
      }
    }, 1000);
  } catch (error: any) {
    dispatch({ type: failWeb, payload: error.toString() });
  }
}

export async function getTodoList(dispatch: any, queryParams: string) {
  try {
    // начинается загрузка
    dispatch({ type: constants.todoList.load });
    const response = await axios.get(
      `https://jsonplaceholder.typicode.com/todos${queryParams}`
    );
    setTimeout(() => {
      if (response.status === 200 || response.status === 201) {
        // если всё успешно
        dispatch({
          type: constants.todoList.success,
          payload: response.data.slice(0, 20),
        });
      } else {
        // если ошибка на backend
        dispatch({
          type: constants.todoList.error,
          payload: response.statusText,
        });
      }
    }, 2000);
  } catch (error: any) {
    // если ошибка на frontend
    dispatch({ type: constants.todoList.fail, payload: error.toString() });
  }
}

export async function getTodoDetail(dispatch: any, id: string | undefined) {
  try {
    dispatch({ type: constants.todoDetail.load });
    const response = await axios.get(
      `https://jsonplaceholder.typicode.com/todos/${id}`
    );
    setTimeout(() => {
      if (response.status === 200 || response.status === 201) {
        dispatch({
          type: constants.todoDetail.success,
          payload: response.data,
        });
      } else {
        dispatch({
          type: constants.todoDetail.error,
          payload: response.statusText,
        });
      }
    }, 100);
  } catch (error: any) {
    dispatch({ type: constants.todoDetail.fail, payload: error.toString() });
  }
}
