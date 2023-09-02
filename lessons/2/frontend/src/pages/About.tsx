import React from "react";
import { Link } from "react-router-dom";
import * as navbars from "../components/ui/navbars";
import * as buttons from "../components/ui/buttons";
import * as bases from "../components/ui/bases";

export default function Page(): JSX.Element {
  return (
    <bases.Base1>
      <Link to={"/"}>на главную</Link>О нас
    </bases.Base1>
  );
}
