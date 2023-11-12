import React from "react";

import * as navbars from "../components/navbars";
import * as footers from "../components/footers";

export default function Page() {
  return (
    <div>
      <navbars.Navbar1 />
      <hr />
      <hr />
      <div>
        <h1>Content</h1>
      </div>
      <hr />
      <hr />
      <footers.Footer1 />
    </div>
  );
}
