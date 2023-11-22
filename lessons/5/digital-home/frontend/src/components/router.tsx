import { BrowserRouter, Routes, Route } from "react-router-dom";
import IndexPage from "../pages/Index";
import DesignPage from "../pages/DesignPage";
import Taiwind from "../pages/Taiwind";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<IndexPage />}></Route>
        <Route path="/design" element={<DesignPage />}></Route>
        <Route path="/design2" element={<Taiwind />}></Route>

        {/*other*/}
        <Route path="*" element={<IndexPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
