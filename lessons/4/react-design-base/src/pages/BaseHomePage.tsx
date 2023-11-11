import React from "react";
//
import * as bases from "../components/ui/bases";
import * as buttons from "../components/ui/buttons";

export default function Page() {
  return (
    <bases.Base1>
      <aside>
        aside
        <buttons.CustomButton1>я кнопка</buttons.CustomButton1>
        <i className="fa-solid fa-arrow-up-from-bracket ms-3 p-1"></i>
      </aside>
      <img
        src={
          "https://img.freepik.com/free-photo/a-cupcake-with-a-strawberry-on-top-and-a-strawberry-on-the-top_1340-35087.jpg"
        }
        alt={"image1"}
      />
      <div>content</div>
    </bases.Base1>
  );
}
