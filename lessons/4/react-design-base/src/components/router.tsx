import { BrowserRouter, Routes, Route } from "react-router-dom";
import BaseHomePage from "../pages/BaseHomePage";
import TailwindCDNPage from "../pages/TailwindCDNPage";
import BootstrapNativeLibPage from "../pages/BootstrapNativeLibPage";
import MuiLibPage, { SignIn } from "../pages/MuiLibPage";
import AdLoaderPage from "../pages/AdLoaderPage";
import AdVideoPlayerPage from "../pages/AdVideoPlayerPage";
import AdChartsPage from "../pages/AdChartsPage";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        {/*base*/}
        <Route path="/" element={<BaseHomePage />}></Route>
        <Route path="/home" element={<BaseHomePage />}></Route>

        {/*tailwind*/}
        <Route path="/tailwind" element={<TailwindCDNPage />}></Route>

        {/*bootstrap*/}
        <Route path="/bootstrap" element={<BootstrapNativeLibPage />}></Route>

        {/*mui*/}
        <Route path="/mui" element={<SignIn />}></Route>

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
