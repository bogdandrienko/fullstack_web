import * as constants from "../components/constants";
import * as actions from "../components/actions";
import * as utils from "../components/utils";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

export default function Page() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const store = useSelector((store: any) => store.storeUserRegister); // {}
  const [form, setForm] = useState({ username: "", password: "" });

  function sendData(event: any) {
    event.preventDefault();
    if (!store.load) {
      actions.constructorPostAction(
        dispatch,
        constants.constantUserRegister,
        {
          ...form, // * unpuck
          username: form.username,
        },
        `http://127.0.0.1:8000/api/register/`,
      );
    }
  }

  useEffect(() => {
    utils.PrintConsoleLog(store, "store");
    if (store.data && store.data.data) {
      setTimeout(() => {
        navigate("/login");
      }, 2000);
    }
  }, [store]);

  return (
    <div>
      <hr />
      {store.load && "loading..."}
      {store.fail && store.fail}
      {store.error && store.error}
      {store.data && store.data.data && store.data.data}
      <hr />
      <form onSubmit={sendData}>
        <input
          type="text"
          value={form.username}
          onChange={(event) => {
            setForm({ ...form, username: event.target.value });
          }}
        />
        <br />
        <input
          type="password"
          value={form.password}
          onChange={(event) => {
            setForm({ ...form, password: event.target.value });
          }}
        />
        <br />
        <hr />
        <button type={"submit"} disabled={store.load}>
          OK
        </button>
      </form>
    </div>
  );
}
