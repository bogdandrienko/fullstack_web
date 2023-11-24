import * as constants from "../components/constants";
import axios from "axios";
import { useState } from "react";

export default function Page() {
  const [form, setForm] = useState({ username: "", password: "" });

  const [loading, setLoading] = useState(false);
  const [error, setError]: any = useState(undefined);
  const [data, setData]: any = useState(undefined);

  async function sendRegisterData(event: any) {
    try {
      event.preventDefault();
      setData(undefined);
      setLoading(true);
      const response = await axios.post(`http://127.0.0.1:8000/api/register/`, {
        ...form, // * unpuck
        username: form.username,
      });
      setLoading(false);

      console.log("response: ", response);
      if (response.data) {
        setData(response.data);
      } else {
        setData(undefined);
        setError(response.statusText);
      }
    } catch (error: any) {
      setData(undefined);
      setLoading(false);
      setError(error.toString());
      console.error("error: ", error);
    }
  }

  return (
    <div>
      <form onSubmit={sendRegisterData}>
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
        <button type={"submit"}>OK</button>
      </form>
    </div>
  );
}
