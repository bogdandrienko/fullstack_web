import React from "react";
import { Link } from "react-router-dom";

export function Navbar1() {
  return (
    <div>
      <a href={"/"}></a>
      <Link to={"/"} className={""}>
        home
      </Link>
      <br />
      <Link to={"/tailwind"} className={""}>
        tailwind
      </Link>
      <br />
      <Link to={"/bootstrap"} className={""}>
        bootstrap
      </Link>
      <br />
      <Link to={"/mui"} className={""}>
        mui
      </Link>
      <br />
      <Link to={"/loader"} className={""}>
        loader
      </Link>
      <br />
      <Link to={"/video"} className={""}>
        video
      </Link>
      <br />
      <Link to={"/charts"} className={""}>
        charts
      </Link>
      <br />
      <hr />
    </div>
  );
}
