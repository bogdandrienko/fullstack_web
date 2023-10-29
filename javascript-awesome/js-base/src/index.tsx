import React from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import Data from "./1_Base/6Exceptions";

const container = document.getElementById("root")!;
const root = createRoot(container);

root.render(
  // <React.StrictMode>
  <div>
    <Data></Data>
  </div>,
  // </React.StrictMode>
);
