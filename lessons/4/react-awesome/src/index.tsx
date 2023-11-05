import React from "react";
import { createRoot } from "react-dom/client";
import PRPS, { Props1, Props3 } from "./app/1Props";
import { Counter1, Input1, Ul2 } from "./app/2Counter";
import { Api1 } from "./app/3Web";

const container = document.getElementById("root")!;
const root = createRoot(container);

root.render(<Ul2 />);
