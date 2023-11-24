import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { Navbar, NavDropdown } from "react-bootstrap";
import * as constants from "../components/constants";
import axios from "axios";

// <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

function Footer2(): JSX.Element {
  return (
    <footer className="custom_footer_2 footer mt-auto m-0 p-0 pt-3">
      <div className="bg-dark custom-background-transparent-hard shadow-lg m-0 p-0">
        <ul className="row row-cols-auto row-cols-md-auto row-cols-lg-auto nav justify-content-center m-0 p-0">
          <li className="m-0 p-1">
            <a className="btn btn-sm btn-outline-secondary text-white" href="#">
              <i className="fa fa-arrow-up">{"  "} вверх</i>
              {"  "}
              <i className="fa fa-arrow-up"> </i>
            </a>
          </li>
          <li className="m-0 p-1">
            <Navbar className="dropup m-0 p-0">
              <NavDropdown
                title={
                  <span className="btn-outline-primary text-white">
                    Ссылки
                    <i className="fa-solid fa-circle-info m-0 p-1" />
                  </span>
                }
                id="basic-nav-dropdown-1"
                className="btn btn-sm btn-outline-primary m-0 p-0"
              >
                <li>
                  <strong className="dropdown-header">Сайты</strong>
                  <NavDropdown.Item
                    className="dropdown-item"
                    href="https://kgpasd.polymetal.ru/"
                  >
                    АСД "Полина"
                  </NavDropdown.Item>
                  <NavDropdown.Item
                    className="dropdown-item"
                    href="https://in.polymetal.ru/"
                  >
                    Портал Полиметалла
                  </NavDropdown.Item>
                  <NavDropdown.Item
                    className="dropdown-item"
                    href="http://172.30.23.16:8002/"
                  >
                    Цифровой Двойник
                  </NavDropdown.Item>
                  <NavDropdown.Item
                    className="dropdown-item"
                    href="http://172.30.23.16:8003/"
                  >
                    Цифровой Двойник Тест
                  </NavDropdown.Item>
                  <NavDropdown.Divider />
                </li>
                <li>
                  <strong className="dropdown-header">Социальное</strong>
                  <NavDropdown.Item className="dropdown-item disabled" href="#">
                    ...
                  </NavDropdown.Item>
                  <NavDropdown.Divider />
                </li>
                <li>
                  <strong className="dropdown-header">Адрес</strong>
                  <NavDropdown.Item className="dropdown-item disabled" href="#">
                    ...
                  </NavDropdown.Item>
                  <NavDropdown.Divider />
                </li>
                <li>
                  <strong className="dropdown-header">Тел/факс</strong>
                  <NavDropdown.Item className="dropdown-item disabled" href="#">
                    ...
                  </NavDropdown.Item>
                  <NavDropdown.Divider />
                </li>
                <li>
                  <strong className="dropdown-header">Почта</strong>
                  <NavDropdown.Item className="dropdown-item disabled" href="#">
                    ...
                  </NavDropdown.Item>
                </li>
              </NavDropdown>
            </Navbar>
          </li>
          <li className="m-0 p-1">
            <Navbar className="dropup text-dark m-0 p-0">
              <NavDropdown
                title={
                  <span className="btn-outline-danger text-white">
                    По всем вопросам!
                    <i className="fa-solid fa-truck-medical m-0 p-1" />
                  </span>
                }
                id="basic-nav-dropdown-2"
                className="btn btn-sm btn-outline-danger m-0 p-0"
              >
                <li>
                  <strong className="dropdown-header">
                    Рабочий номер, стационарный
                  </strong>
                  <NavDropdown.Item className="dropdown-item" href="#">
                    (63) 176
                  </NavDropdown.Item>
                  <NavDropdown.Divider />
                </li>
                <li>
                  <strong className="dropdown-header">
                    Рабочий номер, мобильный
                  </strong>
                  <NavDropdown.Item className="dropdown-item" href="#">
                    + 7 771 293 12 37
                  </NavDropdown.Item>
                  <NavDropdown.Divider />
                </li>
                <li>
                  <strong className="dropdown-header">Почта, локальная</strong>
                  <NavDropdown.Item className="dropdown-item" href="#">
                    AndrienkoBN@polymetal.kz
                  </NavDropdown.Item>
                </li>
              </NavDropdown>
            </Navbar>
          </li>
        </ul>
      </div>
    </footer>
  );
}

function Navbar2({
  title,
  description,
}: {
  title: string;
  description: string;
}): JSX.Element {
  return (
    <header className="p-1 m-0 py-1 mb-2 text-bg-dark border-bottom">
      <div className="container d-flex flex-wrap justify-content-center">
        <a
          href="/"
          className="d-flex align-items-center btn btn-outline-danger mb-3 mb-lg-0 me-lg-auto link-body-emphasis text-decoration-none text-white"
        >
          <i className="fa-solid fa-arrows-rotate m-1 p-1"></i>
          <span className="fs-4">перезагрузить</span>
        </a>
        <div className="col-12 col-lg-auto mb-3 mb-lg-0">
          <div className={"input-group"}>
            <Link
              to={"/"}
              className={"btn btn-lg btn-success fw-bold lead display-6"}
            >
              <i className="fa-solid fa-house m-1 p-1"></i>
              на главную страницу
            </Link>
            <Link
              to={"/login"}
              className={
                "btn btn-lg btn-primary disabled fw-bold lead display-6"
              }
            >
              <i className="fa-solid fa-right-to-bracket m-1 p-1"></i>
              войти
            </Link>
          </div>
        </div>
      </div>
      <hr className={"m-2 p-0"} />
      <div className="container d-flex flex-wrap justify-content-center">
        <div className="d-flex align-items-center mb-3 mb-lg-0 me-lg-auto text-white lead">
          {title}
        </div>
        <div className="d-flex align-items-center mb-3 mb-lg-0 me-lg-auto text-white small">
          {description}
        </div>
      </div>
    </header>
  );
}

export function Base2({
  title,
  description,
  children,
}: {
  title: string;
  description: string;
  children: React.ReactNode;
}): JSX.Element {
  return (
    <div className="h-100 m-0 p-0">
      <Navbar2 title={title} description={description} />
      <main className="custom_main_1">{children}</main>
      <Footer2 />
    </div>
  );
}

export function correctZero(chars: string) {
  let result = chars;
  if (result.length === 1) {
    result = `0${result}`;
  }
  return result;
}

function getCurrentDateTime() {
  const dateTime = new Date();

  const day = correctZero(`${dateTime.getDate()}`);
  const month = correctZero(`${dateTime.getMonth() + 1}`);
  const year = `${dateTime.getFullYear()}`;
  const hours = correctZero(`${dateTime.getHours()}`);
  const minutes = correctZero(`${dateTime.getMinutes()}`);
  const seconds = correctZero(`${dateTime.getSeconds()}`);

  return `${day}.${month}.${year} ${hours}:${minutes}:${seconds}`;
}

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

export default function Page(): JSX.Element {
  const store = useSelector((state: any) => state.messageListStore);

  const dispatch = useDispatch();
  const [state, setState]: any = useState({});
  const [currentTime, setCurrentTime] = useState(getCurrentDateTime());
  const [form, setForm] = useState({
    minVal: 180,
    timeDiff: 10,
    danger: false,
    commsHealth: "нет данных",
    commsIsCheck: true,
    asmHealth: "нет данных",
    asmIsCheck: false,
    geoHealth: "нет данных",
    geoIsCheck: false,
    drainageHealth: "нет данных",
    drainageIsCheck: false,
  });

  useEffect(() => {
    console.log(store);
  }, [store]);

  useEffect(() => {
    if (store && store.data) {
      setState(store.data);
    }
  }, [store.data]);
  useEffect(() => {
    getMessageList(dispatch, "");
    setTimeout(async () => {
      setCurrentTime(getCurrentDateTime());
    }, 4000);
  }, [currentTime]);

  useEffect(() => {
    if (state && state.data) {
      let commsHealth = "нет данных";
      if (state.data.pulse) {
        commsHealth = "";
        if (state.data.pulse.message && state.data.pulse.message.param1 < 120) {
          commsHealth = "низкое сердцебиение";
        }
      }
      setForm({
        ...form,
        commsHealth: commsHealth,
      });
    }
  }, [state.data]);

  return (
    <Base2
      title={"СИТУАЦИОННЫЙ ЦЕНТР: Центр мониторинга"}
      description={"Мониторинг критических показателей в реальном времени"}
    >
      {/*TODO Таблица*/}
      <div className={"card m-0 p-0 bg-dark"}>
        {(store.fail === undefined || store.error === undefined) &&
        state &&
        state.data ? (
          <div className={"shadow album p-1"}>
            <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
              <div className={"col"}>
                <div
                  className="dropdown-menu position-static d-flex flex-column flex-lg-row align-items-stretch justify-content-start p-0 rounded-3 shadow-lg"
                  data-bs-theme="dark"
                >
                  <nav
                    className={
                      form.commsHealth !== "" && form.commsIsCheck
                        ? "col-lg-4 bg-danger"
                        : "col-lg-4"
                    }
                  >
                    <ul className="list-unstyled d-flex flex-column text-center text-white">
                      <li>
                        <div>
                          <div className={"text-start"}>
                            <button
                              className={
                                form.commsIsCheck
                                  ? "btn btn-outline-success fa-solid fa-volume-high p-3"
                                  : "btn btn-outline-secondary fa-solid fa-volume-xmark p-3"
                              }
                              onClick={() => {
                                setForm({
                                  ...form,
                                  commsIsCheck: !form.commsIsCheck,
                                });
                              }}
                            ></button>
                          </div>
                          <strong className="d-block">
                            ПОЗИЦИОНИРОВАНИЕ ПЕРСОНАЛА
                          </strong>
                          <small>(буровзрывные работы)</small>
                        </div>
                      </li>
                      {form.commsIsCheck && (
                        <div>
                          <li className={"py-3"}>
                            <div>
                              <strong className="d-block">ВРЕМЯ СВЯЗИ</strong>
                              <small>
                                {state.data.pulse.datetime_server.split(".")[0]}
                              </small>
                            </div>
                          </li>
                          <li className={"py-3"}>
                            <div>
                              <strong className="d-block">СТАТУС</strong>
                              <small
                                className={
                                  form.commsHealth === ""
                                    ? "text-success"
                                    : "text-white lead"
                                }
                              >
                                {form.commsHealth === ""
                                  ? "в норме"
                                  : form.commsHealth}
                              </small>
                            </div>
                          </li>
                        </div>
                      )}
                    </ul>
                  </nav>
                  <div className="d-none d-lg-block vr mx-4 opacity-10">
                    &nbsp;
                  </div>
                  <div className="col-lg-auto">
                    <nav className="m-0 p-0">
                      <table className="table small table-dark m-0 p-0 rounded">
                        <thead>
                          <tr>
                            <th scope="col" className={"text-white"}>
                              Верхний:
                            </th>
                            <th scope="col" className={"text-white"}>
                              Нижний:
                            </th>
                            <th scope="col" className={"text-white"}>
                              Время:
                            </th>
                          </tr>
                        </thead>
                        <tbody>
                          {state.data.pulse.message && (
                            <tr key={state.data.pulse.message.id}>
                              <td className={""}>
                                {state.data.pulse.message.param1}
                              </td>
                              <td className={""}>
                                {state.data.pulse.message.param2}
                              </td>
                              <td className={""}>
                                {
                                  state.data.pulse.message.datetime_iot.split(
                                    ".",
                                  )[0]
                                }
                              </td>
                            </tr>
                          )}
                        </tbody>
                      </table>
                    </nav>
                  </div>
                </div>
              </div>

              <div className={"col"}>
                <div
                  className="dropdown-menu position-static d-flex flex-column flex-lg-row align-items-stretch justify-content-start p-0 rounded-3 shadow-lg"
                  data-bs-theme="dark"
                >
                  <nav
                    className={
                      form.asmHealth !== "" && form.asmIsCheck
                        ? "col-lg-4 bg-danger"
                        : "col-lg-4"
                    }
                  >
                    <ul className="list-unstyled d-flex flex-column text-center text-white">
                      <li>
                        <div>
                          <div className={"text-start"}>
                            <button
                              className={
                                form.asmIsCheck
                                  ? "btn btn-outline-success fa-solid fa-volume-high p-3"
                                  : "btn btn-outline-secondary fa-solid fa-volume-xmark p-3"
                              }
                              onClick={() => {
                                setForm({
                                  ...form,
                                  asmIsCheck: !form.asmIsCheck,
                                });
                              }}
                            ></button>
                          </div>
                          <strong className="d-block">ЭКОЛОГИЯ</strong>
                          <small>
                            (автоматизированная станция мониторинга)
                          </small>
                        </div>
                      </li>
                      {form.asmIsCheck && (
                        <div>
                          <li className={"py-3"}>
                            <div>
                              <strong className="d-block">ВРЕМЯ СВЯЗИ</strong>
                              <small>
                                {
                                  state.data.communicator_asm.date_time_server.split(
                                    ".",
                                  )[0]
                                }
                              </small>
                            </div>
                          </li>
                          <li className={"py-3"}>
                            <div>
                              <strong className="d-block">СТАТУС</strong>
                              <small
                                className={
                                  form.asmHealth === ""
                                    ? "text-success"
                                    : "text-white lead"
                                }
                              >
                                {form.asmHealth === ""
                                  ? "в норме"
                                  : form.asmHealth}
                              </small>
                            </div>
                          </li>
                        </div>
                      )}
                    </ul>
                  </nav>
                  <div className="d-none d-lg-block vr mx-4 opacity-10">
                    &nbsp;
                  </div>
                  <div className="col-lg-auto">
                    {form.asmHealth !== "" || !form.asmIsCheck ? (
                      "..."
                    ) : (
                      <nav className="m-0 p-0">
                        <table className="table small table-light m-0 p-0 rounded">
                          <thead>
                            <tr>
                              <th scope="col" className={"text-white"}>
                                Наименование:
                              </th>
                              <th scope="col" className={"text-white"}>
                                Время:
                              </th>
                              <th scope="col" className={"text-white"}>
                                Значение:
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            {state.data.communicator_asm.message.map(
                              (item: any, index: number) => (
                                <tr key={item.id}>
                                  <td className={"text-white"}>{item.name}</td>
                                  <td className={"text-white"}>
                                    {item.timestamp.split(".")[0]}
                                  </td>
                                  <td className={"text-white"}>{item.value}</td>
                                </tr>
                              ),
                            )}
                          </tbody>
                        </table>
                      </nav>
                    )}
                  </div>
                </div>
              </div>

              <div className={"col"}>
                <div
                  className="dropdown-menu position-static d-flex flex-column flex-lg-row align-items-stretch justify-content-start p-0 rounded-3 shadow-lg"
                  data-bs-theme="dark"
                >
                  <nav
                    className={
                      form.drainageHealth !== "" && form.drainageIsCheck
                        ? "col-lg-4 bg-danger"
                        : "col-lg-4"
                    }
                  >
                    <ul className="list-unstyled d-flex flex-column text-center text-white">
                      <li>
                        <div>
                          <div className={"text-start"}>
                            <button
                              className={
                                form.drainageIsCheck
                                  ? "btn btn-outline-success fa-solid fa-volume-high p-3"
                                  : "btn btn-outline-secondary fa-solid fa-volume-xmark p-3"
                              }
                              onClick={() => {
                                setForm({
                                  ...form,
                                  drainageIsCheck: !form.drainageIsCheck,
                                });
                              }}
                            ></button>
                          </div>
                          <strong className="d-block">
                            РАСХОДОМЕР ВОДООТЛИВА
                          </strong>
                          <small>(асд)</small>
                        </div>
                      </li>
                      {form.drainageIsCheck && (
                        <div>
                          <li className={"py-3"}>
                            <div>
                              <strong className="d-block">ВРЕМЯ СВЯЗИ</strong>
                              <small>
                                {
                                  state.data.communicator_drainage.date_time_server.split(
                                    ".",
                                  )[0]
                                }
                              </small>
                            </div>
                          </li>
                          <li className={"py-3"}>
                            <div>
                              <strong className="d-block">СТАТУС</strong>
                              <small
                                className={
                                  form.drainageHealth === ""
                                    ? "text-success"
                                    : "text-white lead"
                                }
                              >
                                {form.drainageHealth === ""
                                  ? "в норме"
                                  : form.drainageHealth}
                              </small>
                            </div>
                          </li>
                        </div>
                      )}
                    </ul>
                  </nav>
                  <div className="d-none d-lg-block vr mx-4 opacity-10">
                    &nbsp;
                  </div>
                  <div className="col-lg-auto">
                    {!form.drainageIsCheck ? (
                      "..."
                    ) : (
                      <nav className="m-0 p-0">
                        <table className="table small table-light m-0 p-0 rounded">
                          <thead>
                            <tr>
                              <th scope="col" className={"text-white"}>
                                Время:
                              </th>
                              <th scope="col" className={"text-white"}>
                                Значение:
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td className={"text-white"}>
                                {
                                  state.data.communicator_drainage.message
                                    .maxtime
                                }
                              </td>
                              <td className={"text-white"}>
                                {
                                  state.data.communicator_drainage.message
                                    .maxfuel
                                }
                              </td>
                            </tr>
                            <tr>
                              <td className={"text-white"}>
                                {
                                  state.data.communicator_drainage.message
                                    .mintime
                                }
                              </td>
                              <td className={"text-white"}>
                                {
                                  state.data.communicator_drainage.message
                                    .minfuel
                                }
                              </td>
                            </tr>
                            <tr>
                              <td colSpan={2} className={"text-white"}>
                                Производительность(в час):{" "}
                                {state.data.communicator_drainage.message
                                  .difval < 180 ? (
                                  <span
                                    className={
                                      "text-danger lead fw-bold m-0 p-0 text-white"
                                    }
                                  >
                                    {
                                      state.data.communicator_drainage.message
                                        .difval
                                    }
                                  </span>
                                ) : state.data.communicator_drainage.message
                                    .difval -
                                    20 <
                                  180 ? (
                                  <span
                                    className={
                                      "text-warning lead fw-bold m-0 p-0 text-white"
                                    }
                                  >
                                    {
                                      state.data.communicator_drainage.message
                                        .difval
                                    }
                                  </span>
                                ) : (
                                  <span
                                    className={
                                      "text-success lead fw-bold m-0 p-0 text-white"
                                    }
                                  >
                                    {
                                      state.data.communicator_drainage.message
                                        .difval
                                    }
                                  </span>
                                )}
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </nav>
                    )}
                  </div>
                </div>
              </div>

              <div className={"col"}>
                <div
                  className="dropdown-menu position-static d-flex flex-column flex-lg-row align-items-stretch justify-content-start p-0 rounded-3 shadow-lg"
                  data-bs-theme="dark"
                >
                  <nav
                    className={
                      form.geoHealth !== "" && form.geoIsCheck
                        ? "col-lg-4 bg-danger"
                        : "col-lg-4"
                    }
                  >
                    <ul className="list-unstyled d-flex flex-column text-center text-white">
                      <li>
                        <div>
                          <div className={"text-start"}>
                            <button
                              className={
                                form.geoIsCheck
                                  ? "btn btn-outline-success fa-solid fa-volume-high p-3"
                                  : "btn btn-outline-secondary fa-solid fa-volume-xmark p-3"
                              }
                              onClick={() => {
                                setForm({
                                  ...form,
                                  geoIsCheck: !form.geoIsCheck,
                                });
                              }}
                            ></button>
                          </div>
                          <strong className="d-block">
                            ДВИЖЕНИЕ БОРТОВ КАРЬЕРА
                          </strong>
                          <small>(маркшейдеры)</small>
                        </div>
                      </li>
                      <li className={"py-3"}>
                        <div>
                          <strong className="d-block">ВРЕМЯ СВЯЗИ</strong>
                          <small>--.--.---- --:--:--</small>
                        </div>
                      </li>
                      <li className={"py-3"}>
                        <div>
                          <strong className="d-block">СТАТУС</strong>
                          <small className={"text-secondary"}>
                            в разработке
                          </small>
                        </div>
                      </li>
                    </ul>
                  </nav>
                  <div className="d-none d-lg-block vr mx-4 opacity-10">
                    &nbsp;
                  </div>
                  <div className="col-lg-auto">...</div>
                </div>
              </div>

              <div className={"col"}>
                <div
                  className="dropdown-menu position-static d-flex flex-column flex-lg-row align-items-stretch justify-content-start p-0 rounded-3 shadow-lg"
                  data-bs-theme="dark"
                >
                  <nav className="col-lg-4">
                    <ul className="list-unstyled d-flex flex-column text-center text-white">
                      <li>
                        <div>
                          <div className={"text-start"}>
                            <button className="btn btn-outline-secondary fa-solid fa-volume-xmark p-3"></button>
                          </div>
                          <strong className="d-block">
                            МОНИТОРИНГ УСТАЛОСТИ ПЕРСОНАЛА
                          </strong>
                          <small>(умные камеры)</small>
                        </div>
                      </li>
                      <li className={"py-3"}>
                        <div>
                          <strong className="d-block">ВРЕМЯ СВЯЗИ</strong>
                          <small>--.--.---- --:--:--</small>
                        </div>
                      </li>
                      <li className={"py-3"}>
                        <div>
                          <strong className="d-block">СТАТУС</strong>
                          <small className={"text-secondary"}>
                            в разработке
                          </small>
                        </div>
                      </li>
                    </ul>
                  </nav>
                  <div className="d-none d-lg-block vr mx-4 opacity-10">
                    &nbsp;
                  </div>
                  <div className="col-lg-auto">...</div>
                </div>
              </div>

              <div className={"col"}>
                <div
                  className="dropdown-menu position-static d-flex flex-column flex-lg-row align-items-stretch justify-content-start p-0 rounded-3 shadow-lg"
                  data-bs-theme="dark"
                >
                  <nav className="col-lg-4">
                    <ul className="list-unstyled d-flex flex-column text-center text-white">
                      <li>
                        <div>
                          <div className={"text-start"}>
                            <button className="btn btn-outline-secondary fa-solid fa-volume-xmark p-3"></button>
                          </div>
                          <strong className="d-block">
                            УЧЁТ ЭЛЕКТРО - ЭНЕРГИИ
                          </strong>
                          <small>(энергетики)</small>
                        </div>
                      </li>
                      <li className={"py-3"}>
                        <div>
                          <strong className="d-block">ВРЕМЯ СВЯЗИ</strong>
                          <small>--.--.---- --:--:--</small>
                        </div>
                      </li>
                      <li className={"py-3"}>
                        <div>
                          <strong className="d-block">СТАТУС</strong>
                          <small className={"text-secondary"}>
                            в разработке
                          </small>
                        </div>
                      </li>
                    </ul>
                  </nav>
                  <div className="d-none d-lg-block vr mx-4 opacity-10">
                    &nbsp;
                  </div>
                  <div className="col-lg-auto">...</div>
                </div>
              </div>

              <div className={"col"}>
                <div
                  className="dropdown-menu position-static d-flex flex-column flex-lg-row align-items-stretch justify-content-start p-0 rounded-3 shadow-lg"
                  data-bs-theme="dark"
                >
                  <nav className="col-lg-4">
                    <ul className="list-unstyled d-flex flex-column text-center text-white">
                      <li>
                        <div>
                          <div className={"text-start"}>
                            <button className="btn btn-outline-secondary fa-solid fa-volume-xmark p-3"></button>
                          </div>
                          <strong className="d-block">
                            ПОЖАРНАЯ БЕЗОПАСНОСТЬ
                          </strong>
                          <small>(удалённые пульты ПБ)</small>
                        </div>
                      </li>
                      <li className={"py-3"}>
                        <div>
                          <strong className="d-block">ВРЕМЯ СВЯЗИ</strong>
                          <small>--.--.---- --:--:--</small>
                        </div>
                      </li>
                      <li className={"py-3"}>
                        <div>
                          <strong className="d-block">СТАТУС</strong>
                          <small className={"text-secondary"}>
                            в разработке
                          </small>
                        </div>
                      </li>
                    </ul>
                  </nav>
                  <div className="d-none d-lg-block vr mx-4 opacity-10">
                    &nbsp;
                  </div>
                  <div className="col-lg-auto">...</div>
                </div>
              </div>
            </div>
          </div>
        ) : (
          <div
            className={
              "display-1 text-bg-light text-center text-danger shadow my-1"
            }
          >
            ДАННЫХ НЕТ!
          </div>
        )}
      </div>
    </Base2>
  );
}
