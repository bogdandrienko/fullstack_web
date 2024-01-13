import React, { useEffect, useState } from "react";
import axios from "axios";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [sendForm, setSendForm] = useState({ text: "" });

  async function GetMessages() {
    try{
      const response = await axios.get(
        "http://localhost:8000/messages?skip=0&limit=100",
      );
      setMessages(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  async function SendMessage(event: React.FormEvent) {
    try{
      event.preventDefault();
      const response = await axios.post("http://localhost:8000/messages", {
        ...sendForm,
      });
      GetMessages();
    } catch (error) {
      console.error(error);
    }
  }

  async function UpdateMessage(id: number) {
    try{
      const response = await axios.put(`http://localhost:8000/messages/${id}`);
      GetMessages();
    } catch (error) {
      console.error(error);
    }
  }

  async function DeleteMessage(id: number) {
    try{
      const response = await axios.delete(`http://localhost:8000/messages/${id}`);
      GetMessages();
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    GetMessages();
  }, []);

  return (
    <div className="">
      <form onSubmit={(event) => SendMessage(event)}>
        <input
          type={"text"}
          name={"text"}
          value={sendForm.text}
          onChange={(event) =>
            setSendForm({ ...sendForm, text: event.target.value })
          }
          placeholder={"введите сюда сообщение"}
          required
        />
        <button type={"submit"}>отправить</button>
      </form>
      <hr />
      <header className="">
        <ul>
          {messages && messages.length > 0 ? (
            messages.map(
              (
                item: { id: number; text: string; created_at: string },
                index,
              ) => (
                <li key={index}>
                  #{index + 1} {item.text} ({item.id} |{" "}
                  {item.created_at.split("T")[1].split(".")[0]})
                  <button onClick={() => UpdateMessage(item.id)}>update</button>
                  <button onClick={() => DeleteMessage(item.id)}>delete</button>
                </li>
              ),
            )
          ) : (
            <li>Данные не получены!</li>
          )}
        </ul>
      </header>
    </div>
  );
}
