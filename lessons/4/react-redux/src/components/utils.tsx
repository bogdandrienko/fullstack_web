import * as constants from "../components/constants";
export function Print(message: any) {
  if (constants.DEBUG) {
    console.log(message);
  }
}
