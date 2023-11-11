import { BrowserRouter, Routes, Route } from "react-router-dom";

// base
import BaseHomePage from "../pages/BaseHomePage";

// tailwind
import TailwindCDNPage from "../pages/TailwindCDNPage";

// react
import ReactNativeLibPage from "../pages/ReactNativeLibPage";

// mui
import MuiLibPage from "../pages/MuiLibPage";

// additions
import AdChartsPage from "../pages/AdChartsPage";
import AdVideoPlayerPage from "../pages/AdVideoPlayerPage";
import AdLoaderPage from "../pages/AdLoaderPage";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        {/*base*/}
        <Route path="/" element={<BaseHomePage />}></Route>
        <Route path="/home" element={<BaseHomePage />}></Route>

        {/*tailwind*/}
        <Route path="/tailwind" element={<TailwindCDNPage />}></Route>

        {/*react*/}
        <Route path="/react" element={<ReactNativeLibPage />}></Route>

        {/*mui*/}
        <Route path="/mui" element={<MuiLibPage />}></Route>

        {/*additions*/}
        <Route path="/loader" element={<AdLoaderPage />}></Route>
        <Route path="/video" element={<AdVideoPlayerPage />}></Route>
        <Route path="/charts" element={<AdChartsPage />}></Route>

        {/*other*/}
        <Route path="*" element={<BaseHomePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
