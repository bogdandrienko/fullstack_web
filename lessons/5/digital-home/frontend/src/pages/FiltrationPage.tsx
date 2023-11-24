import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
//
import * as constants from "../components/constants";
import axios from "axios";

export async function getMessageList(dispatch: any, queryParams: string) {
  try {
    dispatch({ type: constants.messageList.load });
    const config = { Authorization: "Token=token_auth123" };
    const response = await axios.get(
      `http://127.0.0.1:8000/api/pagination${queryParams}`,
      // @ts-ignore
      config,
    );
    console.log("response: ", response);
    if (response.data) {
      dispatch({ type: constants.messageList.success, payload: response.data });
    } else {
      dispatch({
        type: constants.messageList.error,
        payload: response.statusText,
      });
    }
  } catch (error: any) {
    dispatch({ type: constants.messageList.fail, payload: error.toString() });
    console.error("error: ", error);
  }
}

export default function Page() {
  const dispatch = useDispatch();
  const messageListStore = useSelector((state: any) => state.messageListStore);

  const [state, setState] = useState([]);
  const [inputSearch, setInputSearch] = useState("");

  useEffect(() => {
    if (!messageListStore.data) {
      getMessageList(dispatch, "?page=-1");
    }
  }, []);

  useEffect(() => {
    if (messageListStore.data) {
      console.log("messageListStore.data: ", messageListStore.data);
      setState(messageListStore.data);
    }
  }, [messageListStore]);

  useEffect(() => {
    console.log(state);
  }, [state]);

  useEffect(() => {
    if (messageListStore.data && messageListStore.data.data) {
      // TODO BASE /////////////////////////////////////////////////
      let filtered = messageListStore.data.data.filter((obj: any) =>
        obj.name.toLowerCase().includes(inputSearch.toLowerCase()),
      );
      // step
      filtered = messageListStore.data.data.filter((obj: any) =>
        obj.name.toLowerCase().includes(inputSearch.toLowerCase()),
      );
      // TODO BASE /////////////////////////////////////////////////
      setState(filtered);
    }
  }, [inputSearch]);

  function Filtration(newtext: string) {
    let filtered = messageListStore.data.data.filter((obj: any) =>
      obj.name.toLowerCase().includes(newtext.toLowerCase()),
    );
    setState(filtered);
  }

  /*
/api/token/ free => login password
/api/news/ config:{Auth: "Bearer ${142143143}"
{
  "success": "1. сохраняет в store, 2. сохраняется в кукесы(чтобы при перезагрузке "подтянуть")",
  "refresh": "обернуть каждый запрос и в случае его провала с кодом 401, она вызывает refresh, и при успешном refresh заново вызывает"
}
 */

  return (
    <div>
      <div>
        Realtime Search
        <hr />
        <input
          className={""}
          value={inputSearch}
          // onChange={(event) => setInputSearch(event.target.value)}
          onChange={(e) => Filtration(e.target.value)}
        />
        <hr />
        {messageListStore.load && "loading..."}
        {messageListStore.fail && "Обратитесь к администратору"}
        {messageListStore.error && messageListStore.error}
        <hr />
        {state && state.length > 0 ? (
          <ul>
            {state.map((item: any, index: number) => (
              <li key={item.id}>
                <p>
                  #{index + 1} {item.name}
                </p>
              </li>
            ))}
          </ul>
        ) : (
          <div>Данных нет!</div>
        )}
      </div>
    </div>
  );
}
