import { configureStore } from "@reduxjs/toolkit";
import { combineReducers } from "@reduxjs/toolkit";
import thunk from "redux-thunk";
import { reducerSimpleReduxCounter } from "../pages/SimpleReduxCounterPage";
import { reducerSimpleReduxWebPage } from "../pages/SimpleReduxWebPage";

//
import * as reducers from "../components/reducers";
import * as constants from "../components/constants";

export const reducer = combineReducers({
  simpleReduxCounter: reducerSimpleReduxCounter,
  simpleReduxWebPage: reducerSimpleReduxWebPage,
  //
  todoListStore: reducers.constructorReducer(constants.listTodos),
  todoDetailStore: reducers.constructorReducer(constants.detailTodo),
});

const preloadedState = {
  // @ts-ignore
  // userLoginStore: {
  //   data:
  //     accessToken && refreshToken
  //       ? { access: accessToken, refresh: refreshToken }
  //       : undefined,
  // },
};

export const store = configureStore({
  reducer: reducer,
  devTools: process.env.NODE_ENV !== "production",
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
  preloadedState: preloadedState,
});
