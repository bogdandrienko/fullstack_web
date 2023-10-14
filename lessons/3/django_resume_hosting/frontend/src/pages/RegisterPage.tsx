import React, { useEffect, useState } from "react";
import axios from "axios";

export default function RegisterPage() {
  let first_name = "";
  let search = "";
  const [data, setData] = useState([]);

  async function sendData() {
    try {
      const response = await axios.post(`/api/resume/`, {
        first_name: first_name,
      });
      console.log(response);
      if (response.status === 201) {
        getData();
      }
    } catch (error) {
      console.error(error);
    }
  }

  async function getData() {
    try {
      const response = await axios.get(`/api/resume/?search=${search}`);
      setData(response.data.list);
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    getData();
  }, []);

  return (
    <div>
      <form
        onSubmit={(event) => {
          event.preventDefault();
          sendData();
        }}
      >
        <div>Введите Ваше имя:</div>
        <input
          type="text"
          required
          minLength={4}
          onChange={(event) => {
            event.preventDefault();
            first_name = event.target.value;
          }}
        />
        <button type={"submit"}>Отправить</button>
      </form>

      <hr />
      <hr />
      <hr />
      <div>
        <input
          type="text"
          onChange={(event) => {
            event.preventDefault();
            search = event.target.value;
          }}
        />
        <button onClick={getData}>Получить данные</button>
      </div>
      <ul>
        {data &&
          data.length > 0 &&
          data.map((item: any, index: number) => (
            <li key={index}>
              {item.first_name} {item.id}
            </li>
          ))}
      </ul>
    </div>
  );
}
