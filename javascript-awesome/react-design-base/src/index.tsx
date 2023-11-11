import React from "react";
import { createRoot } from "react-dom/client";
import "./css/my.css";
import "./css/font_awesome/css/all.css";
import "./css/bootstrap/bootstrap.min.css";
//
import Router from "./components/router";

// statis:
// cdn (проблемы с js)
// file (проблемы с js)
// lib

createRoot(document.getElementById("root")!).render(<Router />);
