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
import AnotherReduxPage from "./pages/AnotherReduxPage";

// todos
import TodoListReduxPage from "./pages/TodoListReduxPage";
import TodoDetailReduxPage from "./pages/TodoDetailReduxPage";

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
        <Route path="/another_redux" element={<AnotherReduxPage />}></Route>

        {/*todos*/}
        <Route path="/todos" element={<TodoListReduxPage />}></Route>
        <Route path="/todos/:id" element={<TodoDetailReduxPage />}></Route>
      </Routes>
    </BrowserRouter>
  </Provider>
);
