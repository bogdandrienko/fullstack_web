import { BrowserRouter, Routes, Route } from "react-router-dom";
import IndexPage from "../pages/Index";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<IndexPage />}></Route>

        {/*other*/}
        <Route path="*" element={<IndexPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
