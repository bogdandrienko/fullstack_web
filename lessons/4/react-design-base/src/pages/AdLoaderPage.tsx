import React, { useEffect, useState } from "react";
import axios from "axios";

export function Loader1() {
  return (
    <div className="justify-content-center text-center d-flex">
      <div className="loader_2" />
    </div>
  );
}
export function Error1() {
  return (
    <div className="btn btn-danger">
      <div
        className="mb-3 inline-flex w-full items-center rounded-lg bg-danger-100 px-6 py-5 text-base text-danger-700"
        role="alert"
      >
        <span className="mr-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="currentColor"
            className="h-5 w-5"
          >
            <path
              fill-rule="evenodd"
              d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25zm-1.72 6.97a.75.75 0 10-1.06 1.06L10.94 12l-1.72 1.72a.75.75 0 101.06 1.06L12 13.06l1.72 1.72a.75.75 0 101.06-1.06L13.06 12l1.72-1.72a.75.75 0 10-1.06-1.06L12 10.94l-1.72-1.72z"
              clip-rule="evenodd"
            />
          </svg>
        </span>
        A simple danger alert - check it out!
      </div>
    </div>
  );
}

export const Loader2 = () => {
  return (
    <div className="justify-content-center text-center d-flex">
      <div className="loader_2" />
    </div>
  );
};

export default function Page() {
  let d = "стандарт";
  const [data, setData] = useState([]); //
  // переменная, за которой "следит" react, если она изменяется, он перерендерит блок страницы
  const [isLoading, setIsLoading] = useState(false);

  async function getData() {
    console.log(d);
    d = "новый стандарт";
    console.log(d);

    // loading
    setIsLoading(true);
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/todos",
    );
    setTimeout(() => {
      setData(response.data);
      // success
      setIsLoading(false);
    }, 2000);
  }

  useEffect(() => {
    console.log("page loaded");
    getData();
  }, []); // dependencies
  // следит за dependencies, и вызывает стрелочную функцию при изменении

  return (
    <div>
      {d}
      <button className={"btn btn-primary"} onClick={getData}>
        getData
      </button>

      <div>
        <Error1 />
        <br />
        <hr />
        {isLoading && <Loader1 />}
        {isLoading ? <Loader1 /> : "загрузка не идёт"}
        <hr />
      </div>

      {data && data.length > 0 ? (
        <ul>
          {data.map((item: any, index: number) => (
            <li>{item.title}</li>
          ))}
        </ul>
      ) : (
        <div>
          <br />
          <hr />
          No data
        </div>
      )}
    </div>
  );
}
