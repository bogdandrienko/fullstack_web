import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

export const loadWeb = "loadWeb";
export const successWeb = "successWeb";
export const failWeb = "failWeb";
export const errorWeb = "errorWeb";
export const resetWeb = "resetWeb";

export function reducerSimpleReduxWebPage(
  state = {},
  action: { type: string; payload: any }
) {
  switch (action.type) {
    case loadWeb:
      return { load: true, data: undefined, error: undefined };
    case successWeb:
      return { load: false, data: action.payload, error: undefined };
    case failWeb:
      return { load: false, data: undefined, error: action.payload };
    case errorWeb:
      return { load: false, data: undefined, error: action.payload };
    case resetWeb:
      return { load: undefined, data: undefined, error: undefined };
    default:
      return state;
  }
}

export default function Page() {
  const dispatch = useDispatch();
  const simpleReduxWebPage = useSelector(
    (state: any) => state.simpleReduxWebPage
  );

  async function getData() {
    try {
      dispatch({ type: loadWeb });
      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/todos"
      );
      setTimeout(() => {
        if (response.status === 200 || response.status === 201) {
          dispatch({ type: successWeb, payload: response.data });
        } else {
          dispatch({ type: errorWeb, payload: response.statusText });
        }
      }, 1000);
    } catch (error: any) {
      dispatch({ type: failWeb, payload: error.toString() });
    }
  }

  return (
    <div>
      <button onClick={getData}>getData</button>
      <div className={"container container-fluid text-center"}>
        {simpleReduxWebPage.load === true && (
          <div className={"small fw-light"}>Идёт загрузка</div>
        )}
        {simpleReduxWebPage.fail && (
          <div className={"small fw-light"}>Обратитесь к администатору</div>
        )}
        {simpleReduxWebPage.error && (
          <div className={"small fw-light"}>{simpleReduxWebPage.error}</div>
        )}
        <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
          {!simpleReduxWebPage.data ? (
            "данных пока нет"
          ) : (
            <ul>
              {simpleReduxWebPage.data.map((item: any, index: number) => (
                <li key={item.id}>{item.title}</li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}
