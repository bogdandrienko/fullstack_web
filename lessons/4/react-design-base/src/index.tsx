import React from "react";
import { createRoot } from "react-dom/client";
import "./css/my.css";
import "./css/font_awesome/css/all.css";
import "./css/bootstrap/bootstrap.min.css";
//
import Router from "./components/router";

// static(файлы, которые не подгружаются пользователями - css, js, image, logo):
// cdn (проблемы с js)
// files (проблемы с js)
// lib

createRoot(document.getElementById("root")!).render(<Router />);
