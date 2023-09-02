import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "../pages/Home";
import About from "../pages/About";
import React from "react";

export default function Router1() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={"/"} element={<Home />} />
        <Route path={"/about"} element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}

export const Router2 = () => <div>3333333333333</div>;

export function Router3() {
  return <div>3333333333333</div>;
}
