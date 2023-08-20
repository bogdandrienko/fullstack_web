from datetime import datetime
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
import sqlite3

# Create your views here.


def home(request):
    return HttpResponse(f"home")


def get_string(request):
    value = 12
    return HttpResponse(f"get_string {value}")  # interpolation


class CustomHttpRequest(HttpRequest):  # middleware
    def __init__(self):
        super().__init__()
        self.nikita = list(self.body)


def get_html_string(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>get_html_string</h1>" + "<li>123</li>")  # concatenation


def get_json(request) -> JsonResponse:
    # if request.method == "GET":
    return JsonResponse(
        data={
            "data": False,
            "d": {"data": False, "value": 12},
            "value": 12,
        },
        safe=False,
    )  # concatenation


def get_html_file(request: HttpRequest) -> HttpResponse:
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
    return render(request, "html_file.html", context=context)


def get_dynamic(request: HttpRequest, ml: str = -1) -> HttpResponse:  # != /get_dynamic
    return HttpResponse(f"<h1>data: {ml}</h1>")


def get_args(request: HttpRequest) -> HttpResponse:  # http://127.0.0.1:8000/get_args?passport_id=666
    print(type(request.GET), request.GET)
    # print(type(request.POST), request.POST)
    # print(type(request.FILES), request.FILES)

    # passport_id = request.args["passport_id"]  # args is not exist == Exception

    # passport_id = request.args.get('passport_id', default=None)
    # if passport_id is None:
    #     raise Exception("salary is None")

    passport_id = request.GET.get("passport_id", "Аноним")
    return HttpResponse(f"<h1>passport_id: {passport_id}</h1>")


def get_html_form(request: HttpRequest) -> HttpResponse:
    context = {"result": ""}
    if request.method == "POST":
        print("Отправка")

        text = request.POST.get("text", "")
        datetime_ = request.POST.get("datetime", datetime.now().strftime("%Y-%m-%dT%H:%M"))
        print(type(datetime_), datetime_)  # <class 'str'> 2023-08-10T13:25
        date_object = datetime.strptime(datetime_, "%Y-%m-%dT%H:%M")  # str -> datetime
        print(type(date_object), date_object)
        date_str = date_object.strftime("%H:%M:%S")  # datetime -> str
        print(type(date_str), date_str)

        print(type(request.FILES), request.FILES)
        uploaded_file = request.FILES.get("file", None)  # FileStorage
        print("\n\n\n file: ", uploaded_file)

        context["result"] = text
    return render(request, "get_html_form.html", context=context)
