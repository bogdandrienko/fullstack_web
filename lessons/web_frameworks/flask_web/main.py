import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(
    __name__,
    template_folder="templates",
    static_url_path="/static",
    static_folder="static",
)


@app.route("/get_string")
def get_string():
    value = 12
    return f"get_string {value}"  # interpolation


@app.route("/get_html_string")
def get_html_string():
    return "<h1>get_html_string</h1>" + "<li>123</li>"  # concatenation


@app.route("/get_json")
def get_json():
    elem1 = 8
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in list1:  # O(n) - линейная
        if i == elem1:
            print("find!")

    # list1.sort()
    # list_sorted = sorted(list1)  # O(n*log(N))

    # const params = {"name": "Nikita", ...}
    # params.name

    return {
        "data": False,
        "d": {"data": False, "value": 12},
        "value": 12,
    }  # O(1) - константная


@app.route("/get_html_file")
def get_html_file():
    name = "Python"
    params = {"name": "Nikita", "age": 666}
    list_users: list[dict] = []
    for i in range(1, 100 + 1):
        new_dict = {"id": i, "username": f"User {i}"}
        list_users.append(new_dict)

    is_active = False

    context = {
        "name": name,
        "params": params,
        "is_active": is_active,
        "list_users": list_users,
    }

    return render_template("html_file.html", **context)


@app.route("/get_dynamic/<string:ml>")  # != /get_dynamic
def get_dynamic(ml="1"):
    return f"<h1>data: {ml}</h1>"


@app.route("/get_args")
def get_args():  # http://127.0.0.1:8000/get_args?passport_id=666
    print(type(request.args), request.args)

    # passport_id = request.args["passport_id"]  # args is not exist == Exception

    # passport_id = request.args.get('passport_id', default=None)
    # if passport_id is None:
    #     raise Exception("salary is None")

    passport_id = request.args.get("passport_id", "Аноним")
    return f"<h1>data: {passport_id}</h1>"


@app.route("/get_html_form", methods=["GET", "POST"])
def get_html_form():
    context = {"result": ""}
    if request.method == "POST":
        print("Отправка")

        text = request.form.get("text", "")
        datetime_ = request.form.get(
            "datetime", datetime.now().strftime("%Y-%m-%dT%H:%M")
        )
        print(type(datetime_), datetime_)  #  <class 'str'> 2023-08-10T13:25
        date_object = datetime.strptime(datetime_, "%Y-%m-%dT%H:%M")  # str -> datetime
        print(type(date_object), date_object)
        date_str = date_object.strftime("%H:%M:%S")  # datetime -> str
        print(type(date_str), date_str)

        print(type(request.files), request.files)
        uploaded_file = request.files.get("file", None)  # FileStorage
        print("\n\n\n file: ", uploaded_file)

        context["result"] = text

    return render_template("get_html_form.html", **context)


@app.route("/get_data_from_db", methods=["GET", "POST"])
def get_data_from_db():
    query = """
CREATE TABLE IF NOT EXISTS users
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT
)
"""
    # MSSQL - SSMS
    # ORACLE - TOAD
    # PostgreSQL - PgAdmin
    # MySQL - PhpMyAdmin, MySQL Workbench
    # ...

    # fast / explain(анализ запроса) / --> database
    # ORM -> упрощение(like, where, select...) --> Raw SQL

    with sqlite3.connect("database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute(
            query
            # "SELECT name FROM sqlite_master WHERE type='table';"
        )  # , kwargs)  # todo SQL injection SAFE
        tables = cursor.fetchall()
        print("\n\n tables: ", tables)
        # if many:
        #     return cursor.fetchall()
        # return [cursor.fetchone()]
    return f"<h1>database</h1>"
