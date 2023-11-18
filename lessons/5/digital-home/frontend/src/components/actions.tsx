import * as constants from "./constants";
import axios from "axios";

export async function getMessageList(dispatch: any, queryParams: string) {
  try {
    dispatch({ type: constants.messageList.load });
    const config = { Authorization: "Token=token_auth123" };
    const response = await axios.get(
      `http://127.0.0.1:8000/api/communicator${queryParams}`,
      // @ts-ignore
      config,
    );
    if (response.data) {
      dispatch({ type: constants.messageList.success, payload: response.data });
    } else {
      dispatch({
        type: constants.messageList.error,
        payload: response.statusText,
      });
    }
  } catch (error: any) {
    dispatch({ type: constants.messageList.fail, payload: error.toString() });
    console.error("error: ", error);
  }
}

//
// export function getAllTodos() {
//   return constructorAction({
//     url: `https://jsonplaceholder.typicode.com/todos/`,
//     constant: constants.listTodos,
//   });
// }
//
// export function constructorAction(
//   props = {
//     // @ts-ignore
//     url,
//     constant: {
//       // @ts-ignore
//       load: string,
//       // @ts-ignore
//       success: string,
//       // @ts-ignore
//       fail: string,
//       // @ts-ignore
//       error: string,
//       // @ts-ignore
//       reset: string,
//     },
//   }
// ) {
//   return async function (dispatch: any) {
//     try {
//       // TODO load
//       dispatch({ type: props.constant.load });
//       const response = await axios.get(props.url); // todo откуда берём данные
//       if (response.status === 200 || response.status === 201) {
//         // TODO success
//         dispatch({
//           type: props.constant.success, // todo куда ложим успешные данные
//           payload: response.data,
//         });
//       } else {
//         // TODO error
//         dispatch({
//           type: props.constant.error,
//           payload: response.statusText,
//         });
//       }
//     } catch (error) {
//       console.log("error: ", error);
//       // TODO fail
//       dispatch({
//         type: props.constant.fail,
//         // @ts-ignore
//         payload: error.toString(),
//       });
//     }
//   };
// }
