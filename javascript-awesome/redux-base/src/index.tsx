import React from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { store } from "./app/store";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./css/bootstrap/bootstrap.css";

// base
import HomePage from "./pages/HomePage";

// simple
import SimpleCounterPage from "./pages/SimpleCounterPage";
import SimpleReduxCounterPage from "./pages/SimpleReduxCounterPage";
import SimpleReduxWebPage from "./pages/SimpleReduxWebPage";

// todos
import TodoList from "./pages/TodoList";
import TodoDetail from "./pages/TodoDetail";

createRoot(document.getElementById("root")!).render(
  <Provider store={store}>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />}></Route>
        <Route path="/counter" element={<SimpleCounterPage />}></Route>
        <Route
          path="/counter_redux"
          element={<SimpleReduxCounterPage />}
        ></Route>
        <Route path="/web_redux" element={<SimpleReduxWebPage />}></Route>

        {/*todos*/}
        <Route path="/todos" element={<TodoList />}></Route>
        <Route path="/todos/:id" element={<TodoDetail />}></Route>
      </Routes>
    </BrowserRouter>
  </Provider>
);
