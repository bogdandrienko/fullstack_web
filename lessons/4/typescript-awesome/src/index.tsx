import React from "react";
import { createRoot } from "react-dom/client";
import Data from "./app/1base";
import Ex from "./app/4props";

const container = document.getElementById("root")!;
const root = createRoot(container);

function App() {
  return <div>App</div>;
}

root.render(<Ex />);
