import React from "react";
import * as navbars from "./navbars";

export function Base1({ children }: any) {
  return (
    <div>
      <header>
        <navbars.Navbar1 />
      </header>
      <main>
        <h1 className="custom-div">ЗАГОЛОВОК</h1>
        {children}
      </main>
      <footer>FOOTER 2</footer>
    </div>
  );
}
