import { configureStore } from "@reduxjs/toolkit";
import { combineReducers } from "@reduxjs/toolkit";
import thunk from "redux-thunk";
import { reducerSimpleReduxCounter } from "../pages/SimpleReduxCounterPage";
import { reducerSimpleReduxWebPage } from "../pages/SimpleReduxWebPage";
import { ReducerAnotherReduxPage } from "../components/navbars";

//
import * as reducers from "../components/reducers";
import * as constants from "../components/constants";

export const reducer = combineReducers({
  simpleReduxCounter: reducerSimpleReduxCounter, // useSelector((state: any) => state.simpleReduxCounter);
  simpleReduxWebPage: reducerSimpleReduxWebPage,
  storeAnotherReduxPage: ReducerAnotherReduxPage,
  storeTodoList: reducers.constructorReducerStore(constants.todoList), // TODO initial value
  storeTodoDetail: reducers.constructorReducerStore(constants.todoDetail),
  //
  // todoListStore: reducers.constructorReducer(constants.listTodos),
  // todoDetailStore: reducers.constructorReducer(constants.detailTodo),
});

const preLoadedState = {
  // userLoginStore: {
  //   data: undefined,
  // accessToken && refreshToken
  //   ? { access: accessToken, refresh: refreshToken }
  //   : undefined,
  // },
};

export const store = configureStore({
  reducer: reducer,
  devTools: process.env.NODE_ENV !== "production",
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
  preloadedState: preLoadedState,
});
