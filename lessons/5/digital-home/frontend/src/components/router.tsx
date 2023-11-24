import { BrowserRouter, Routes, Route } from "react-router-dom";
import IndexPage from "../pages/Index";
import DesignPage from "../pages/DesignPage";
import Taiwind from "../pages/TaiwindPage";
import ChartPage from "../pages/ChartPage";
import CurrentPage from "../pages/CurrentPage";
import FiltrationPage from "../pages/FiltrationPage";
import PaginationPage from "../pages/PaginationPage";
import RegisterNativePage from "../pages/RegisterNativePage";
import RegisterReduxPage from "../pages/RegisterReduxPage";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<IndexPage />}></Route>
        <Route path="/design" element={<DesignPage />}></Route>
        <Route path="/design2" element={<Taiwind />}></Route>
        <Route path="/chart" element={<ChartPage />}></Route>
        <Route path="/current" element={<CurrentPage />}></Route>
        <Route path="/filtr" element={<FiltrationPage />}></Route>
        <Route path="/page" element={<PaginationPage />}></Route>
        <Route path="/register_native" element={<RegisterNativePage />}></Route>
        <Route path="/register" element={<RegisterReduxPage />}></Route>

        {/*other*/}
        <Route path="*" element={<IndexPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
