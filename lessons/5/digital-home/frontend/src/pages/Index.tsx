import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
//
import * as base from "../components/ui/base";
import * as actions from "../components/actions";
import * as constants from "../components/constants";

export default function Page() {
  const dispatch = useDispatch();
  const nowMessageListStore = useSelector(
    (state: any) => state.nowMessageListStore,
  );
  const [state, setState]: any = useState(null);
  const [timer, setTimer] = useState(new Date().toString());

  useEffect(() => {
    if (nowMessageListStore.data) {
      setState(nowMessageListStore.data);
    }
  }, [nowMessageListStore.data]);

  useEffect(() => {
    if (constants.DEBUG) {
      console.log("nowMessageListStore: ", nowMessageListStore);
    }
  }, [nowMessageListStore]);

  useEffect(() => {
    if (constants.DEBUG) {
      console.log("state: ", state);
    }
  }, [state]);

  // useEffect(() => {
  //   if (!nowMessageListStore.data) {
  //     getData();
  //   }
  // }, []);

  useEffect(() => {
    getData();
    // console.log("ИЗ ОПЕРАТИВЫ: ", timer);
  }, [timer]);

  function getData() {
    if (!nowMessageListStore.load) {
      actions.constructorAction(
        constants.nowMessageList,
        dispatch,
        `http://127.0.0.1:8000/api/communicator`,
        `?page=1`,
      )(); // carrying

      // console.log("ИЗ РЕКУРСИИ: ", timer);
      setTimeout(() => {
        // getData();  // ВНЕШНЯЯ ЗАВИСИМОСТЬ
        setTimer(new Date().toString());
      }, 3000);
    } else {
      console.log("ЗАГРУЗКА ВСЁ ЕЩЁ ИДЁТ!");
    }
  }

  // @ts-ignore
  return (
    <base.Base1 title={"Домашняя страница"}>
      Index
      <button
        onClick={() => {
          getData();
        }}
        disabled={nowMessageListStore.load}
      >
        getMessageList
      </button>
      <hr />
      {nowMessageListStore.load && !state && "loading..."}
      {nowMessageListStore.fail && "Обратитесь к администратору"}
      {nowMessageListStore.error && nowMessageListStore.error}
      <hr />
      {state && state.data ? (
        <ul>
          {10 === 10 && "ДАААА1111"}
          {10 === 10 ? "ДАААА2222" : "НЕЕЕЕт2222"}
          {state.data.pulse && (
            <li>
              <p>{state.data.pulse.datetime_subsystem.split(".")[0]}</p>
              <p
                className={
                  state.data.pulse.message.param1 > 150
                    ? "text-danger"
                    : "text-secondary"
                }
              >
                {state.data.pulse.message.param1}
              </p>
              {state.data.pulse.message.param2 > 180 ? (
                <h1>{state.data.pulse.message.param2}</h1>
              ) : (
                <p>{state.data.pulse.message.param2}</p>
              )}
            </li>
          )}
          {state.data.voda && (
            <li>
              <p>{state.data.voda.datetime_subsystem.split(".")[0]}</p>
              <p
                className={
                  state.data.voda.message.param1 > 150
                    ? "text-danger"
                    : "text-secondary"
                }
              >
                {state.data.voda.message.param1}
              </p>
            </li>
          )}
        </ul>
      ) : (
        <div>Данных нет!</div>
      )}
    </base.Base1>
  );
}
