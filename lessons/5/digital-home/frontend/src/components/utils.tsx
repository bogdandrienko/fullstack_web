import * as constants from "./constants";

export function PrintConsoleLog(text: any, prefix: string = "") {
  if (constants.DEBUG) {
    console.log(`${prefix}: `, text);
  }
}
