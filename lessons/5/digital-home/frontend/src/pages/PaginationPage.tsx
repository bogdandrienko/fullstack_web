import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import axios from "axios";
import * as constants from "../components/constants";

async function getMessageList(dispatch: any, queryParams: string) {
  try {
    dispatch({ type: constants.messageList.load });
    const config = { Authorization: "Token=token_auth123" };
    const response = await axios.get(
      `http://127.0.0.1:8000/api/pagination${queryParams}`,
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

const GetPagesArray = (totalCount = 0, limit = 1): number[] => {
  try {
    const page = Math.ceil(totalCount / limit);
    let result = [];
    if (totalCount) {
      for (let i = 0; i < page; i++) {
        result.push(i + 1);
      }
    }
    return result;
  } catch (error) {
    return [];
  }
};

interface PaginatorProps {
  totalCount: number;
  limit: number;
  page: number;
  setPage: any; // callback
}

export function PaginatorComponent(props: PaginatorProps) {
  return (
    <div>
      <nav aria-label="Page navigation example">
        <ul className="pagination">
          <li className="page-item">
            <a className="page-link" href="#" aria-label="Previous">
              <span aria-hidden="true">&laquo;</span>
              <span className="sr-only">Previous</span>
            </a>
          </li>
          {GetPagesArray(props.totalCount, props.limit).map((p: number) => (
            <li className="page-item" key={p}>
              <button
                type={"button"}
                className={
                  props.page === p
                    ? "page-link fw-bold bg-warning bg-opacity-75"
                    : "page-link"
                }
                onClick={(event) => {
                  event.preventDefault();
                  event.stopPropagation();
                  props.setPage(p);
                }}
              >
                {p}
              </button>
            </li>
          ))}
          <li className="page-item">
            <a className="page-link" href="#" aria-label="Next">
              <span aria-hidden="true">&raquo;</span>
              <span className="sr-only">Next</span>
            </a>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default function Page() {
  const dispatch = useDispatch();
  const messageListStore = useSelector((state: any) => state.messageListStore);

  const limit = 10;
  const [page, setPage] = useState(1);
  const [totalCount, setTotalCount] = useState(1);

  useEffect(() => {
    if (constants.DEBUG) {
      console.log("messageListStore: ", messageListStore);
    }
    if (messageListStore.data && messageListStore.data.x_total_count > 0) {
      setTotalCount(messageListStore.data.x_total_count);
    }
  }, [messageListStore]);

  useEffect(() => {
    getMessageList(dispatch, `?page=${page}`);
  }, [page]);

  function Callback(p: any) {
    console.log(`НАШ ВОЗВРАТ ${p}`);
  }

  return (
    <div>
      <div>
        Index
        <hr />
        <PaginatorComponent
          totalCount={totalCount}
          limit={limit}
          page={page}
          setPage={setPage}
        />
        <hr />
        <div>
          <nav aria-label="Page navigation example">
            <ul className="pagination">
              <li className="page-item">
                <a className="page-link" href="#" aria-label="Previous">
                  <span aria-hidden="true">&laquo;</span>
                  <span className="sr-only">Previous</span>
                </a>
              </li>
              {GetPagesArray(totalCount, limit).map((p) => (
                <li className="page-item" key={p}>
                  <button
                    type={"button"}
                    className={
                      page === p
                        ? "page-link fw-bold bg-warning bg-opacity-75"
                        : "page-link"
                    }
                    onClick={(event) => {
                      event.preventDefault(); // остановить стандартное поведение
                      event.stopPropagation(); // сброс события вверх
                      setPage(p); // установка page
                    }}
                  >
                    {p}
                  </button>
                </li>
              ))}
              <li className="page-item">
                <a className="page-link" href="#" aria-label="Next">
                  <span aria-hidden="true">&raquo;</span>
                  <span className="sr-only">Next</span>
                </a>
              </li>
            </ul>
          </nav>
        </div>
        <hr />
        {messageListStore.load && "loading..."}
        {messageListStore.fail && "Обратитесь к администратору"}
        {messageListStore.error && messageListStore.error}
        <hr />
        {messageListStore.data &&
        messageListStore.data.data &&
        messageListStore.data.data.length > 0 ? (
          <ul>
            {messageListStore.data.data.map((item: any, index: number) => (
              <li key={item.id}>
                <p>
                  #{item.id} [{item.param1}|{item.param2}]
                </p>
              </li>
            ))}
          </ul>
        ) : (
          <div>Данных нет!</div>
        )}
      </div>
    </div>
  );
}
