import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
//
import * as base from "../components/ui/base";
import * as actions from "../components/actions";
import * as constants from "../components/constants";

export default function Page() {
  const dispatch = useDispatch();
  const messageListStore = useSelector((state: any) => state.messageListStore);
  useEffect(() => {
    if (constants.DEBUG) {
      console.log("messageListStore: ", messageListStore);
    }
  }, [messageListStore]);

  useEffect(() => {
    if (!messageListStore.data) {
      actions.getMessageList(dispatch, "?page=1");
    }
  }, []);

  return (
    <base.Base1 title={"Домашняя страница"}>
      <div>
        Index
        <button
          onClick={() => {
            actions.getMessageList(dispatch, "?page=1");
          }}
        >
          getMessageList
        </button>
        <hr />
        {messageListStore.load && "loading..."}
        {messageListStore.fail && "Обратитесь к администратору"}
        {messageListStore.error && messageListStore.error}
        <hr />
        {messageListStore.data &&
        messageListStore.data.data &&
        messageListStore.data.data.length > 0 ? (
          <ul>
            {messageListStore.data.data.map((item: any, index: number) => (
              <li key={item.id}>
                <p>#{index + 1}</p>
                <p>{item.param1}</p>
                <p>{item.param2}</p>
              </li>
            ))}
          </ul>
        ) : (
          <div>Данных нет!</div>
        )}
      </div>
    </base.Base1>
  );
}
