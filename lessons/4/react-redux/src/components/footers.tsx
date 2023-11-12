import { useSelector } from "react-redux";
import { useEffect } from "react";

import * as contants from "./constants";
import { DEBUG } from "./constants";

export function Footer1() {
  const storeAnotherReduxPage = useSelector(
    (state: any) => state.storeAnotherReduxPage
  );
  useEffect(() => {
    if (contants.DEBUG) {
      console.log(storeAnotherReduxPage);
    }
  }, [storeAnotherReduxPage]);
  return (
    <div>
      {storeAnotherReduxPage.data ? storeAnotherReduxPage.data : "empty"}
      <hr />
      Footer1
    </div>
  );
}
