import React from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { store } from "./app/store";

//
import Router from "./components/router";

//
import "./index.css";
import "./css/bootstrap/bootstrap.css";

const container = document.getElementById("root")!;
const root = createRoot(container);

root.render(
  <Provider store={store}>
    <Router />
  </Provider>,
);
