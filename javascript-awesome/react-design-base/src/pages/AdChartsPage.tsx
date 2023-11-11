import React from "react";
import {
  CartesianGrid,
  Line,
  LineChart,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

export default function Page() {
  const data = [
    { name: "first", value: 10.0 },
    { name: "second", value: 6.0 },
    { name: "third", value: 4.0 },
  ];

  return (
    <div>
      <br />
      <br />
      <br />
      <br />
      <LineChart
        width={900}
        height={150}
        data={data}
        margin={{ top: 0, right: 0, bottom: 0, left: 0 }}
      >
        <Line type="monotone" dataKey="value" stroke="#8884d8" />
        <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
      </LineChart>
    </div>
  );
}
