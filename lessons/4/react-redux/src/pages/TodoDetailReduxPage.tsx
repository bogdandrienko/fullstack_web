import React, { useEffect } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import * as constants from "../components/constants";
import * as utils from "../components/utils";
import * as actions from "../components/actions";
import * as loaders from "../components/ui/loaders";
import * as modals from "../components/ui/modals";
import { Link } from "react-router-dom";

export default function Page() {
  const id = useParams().id;
  const dispatch = useDispatch();
  const storeTodoDetail = useSelector((state: any) => state.storeTodoDetail);
  // const { dataTodoDetail, loadTodoDetail, successTodoDetail } = useSelector(
  //   (state: any) => state.storeTodoDetail
  // ); // декомпозиция

  useEffect(() => {
    actions.getTodoDetail(dispatch, id);
  }, []);

  // print
  useEffect(() => {
    utils.Print(storeTodoDetail);
  }, [storeTodoDetail]);

  return (
    <div>
      TodoDetailReduxPage
      <hr />
      {storeTodoDetail.load && <loaders.Loader1 />}
      {storeTodoDetail.fail && (
        <modals.Fail1>Обратитесь к администратору</modals.Fail1>
      )}
      {storeTodoDetail.error && (
        <modals.Error1>{storeTodoDetail.fail}</modals.Error1>
      )}
      <hr />
      {storeTodoDetail.data ? (
        <div>
          <h1>{storeTodoDetail.data.title}</h1>
          <p>{storeTodoDetail.data.userId}</p>
          <p>{storeTodoDetail.data.id}</p>
          <p>{storeTodoDetail.data.completed ? "выполнено" : "не выполнено"}</p>
        </div>
      ) : (
        <div>Данных нет!</div>
      )}
      <hr />
    </div>
  );
}
