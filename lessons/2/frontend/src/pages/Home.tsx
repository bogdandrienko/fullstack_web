import React from "react";
import { Link } from "react-router-dom";
import * as navbars from "../components/ui/navbars";
import * as buttons from "../components/ui/buttons";
import * as bases from "../components/ui/bases";
import * as constants from "../components/constants";
import axios from "axios";

export default function Page(): JSX.Element {
  function GetSyncData() {
    // XMLHttpRequest
    //   const response = new XMLHttpRequest();

    // const response1 = await fetch("https://jsonplaceholder.typicode.com/todos");
    // @ts-ignore
    // console.log(response1.data);

    axios
      .get("https://jsonplaceholder.typicode.com/todos")
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log("error: ", error);
      });
  }

  async function GetAsyncData() {
    try {
      const response = await axios.get(
        `${constants.SERVER_HOST}/get_todos`,
        // "https://jsonplaceholder.typicode.com/todos",
      );
      if (response.status === 200 || response.status === 201) {
        console.log(response.data);
      } else {
        console.log(response.status);
      }
    } catch (error) {
      if (constants.IS_DEBUG) {
        console.log("error: ", error);
      }
    }
  }

  return (
    <bases.Base1>
      <Link to={"/about"}>о нас</Link>
      <button onClick={GetAsyncData} className={"btn btn-danger p-3"}>
        GetData
      </button>
      Домашняя страница
      <buttons.Button1 color={""}>нажатие!</buttons.Button1>
    </bases.Base1>
  );
}
