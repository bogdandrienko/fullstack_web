import React, { useState } from "react";
import axios from "axios";

// function
const Loader1 = () => {
  return (
    <div className="justify-content-center text-center d-flex">
      <div className="loader_2" />
    </div>
  );
};

export default function Page() {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  async function getData() {
    setIsLoading(true);
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/todos",
    );
    setTimeout(() => {
      setData(response.data);
      setIsLoading(false);
    }, 3000);
  }

  return (
    <div>
      <button className={"btn btn-primary"} onClick={getData}>
        getData
      </button>
      {isLoading ? <Loader1 /> : "загрузка не идёт"}
      {data && data.length > 0 ? (
        <ul>
          {data.map((item: any, index: number) => (
            <li>{item.title}</li>
          ))}
        </ul>
      ) : (
        "No data available"
      )}
    </div>
  );
}
