import re
from datetime import datetime

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse, HttpRequest

from django_app import models


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


######################################################################################

from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def custom_login_required(view: callable):
    def wrapper(*args, **kwargs):  # request: HttpRequest
        request: HttpRequest = args[0]

        if request.user.is_authenticated is False:
            # DRF - return 404
            return redirect(reverse("login"))

        result = view(*args, **kwargs)
        return result

    return wrapper


def home(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "django_app/home.html", context=context)


def login_(request: HttpRequest) -> HttpResponse:
    """Вход в аккаунт пользователя."""

    if request.method == "GET":
        return render(request, "django_app/login.html")
    elif request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=email, password=password)  # standart django auth
        if user is None:  # passport.yandex.com/api/auth/check/?passpordId=1542154234
            return render(request, "django_app/login.html", {"error": "Некорректный email или пароль"})
        login(request, user)  # session_id (cookies)
        return redirect(reverse("home"))


@custom_login_required
def logout_(request: HttpRequest) -> HttpResponse:
    """Выход из аккаунта"""

    logout(request)
    return redirect(reverse("login"))


def track_start(request: HttpRequest) -> HttpResponse:
    """Запуск посылки."""

    if request.method == "GET":
        cities = models.Cities.objects.all().filter(is_active=True, type="0")
        context = {"cities": cities}  # <select options.../>
        return render(request, "django_app/track_start.html", context)
    elif request.method == "POST":
        try:
            target = request.POST["target"]
            weight = request.POST["weight"]
            width = request.POST["width"]
            height = request.POST["height"]
            depth = request.POST["depth"]
            contact = request.POST["contact"]
            address = request.POST["address"]

            models.Item.objects.create(
                track=str(models.Item.track_generator()),
                status="1",
                target=str(target),
                weight=str(weight),
                width=str(width),
                height=str(height),
                depth=str(depth),
                contact=str(contact),
                address=str(address),
                price=models.Item.price_formul(target=target, weight=weight, width=width, height=height, depth=depth),
            )
        except Exception as error:
            return render(
                request,
                "django_app/track_start.html",
                {"error": str(error)},
            )
        return redirect(reverse("track_start"))
    else:
        raise ValueError("Invalid method")


@custom_login_required
def track_find(request: HttpRequest) -> HttpResponse:
    """Поиск посылки."""

    if request.method == "GET":
        return render(request, "django_app/track_find.html", {})
    elif request.method == "POST":
        # request.POST.get("search", "")  # safe
        # request.POST["search"]  # not safe | Exception

        search = str(request.POST.get("search", "")).replace(" ", "").strip()
        try:
            # фильтрация объеков по трек
            item = models.Item.objects.get(track=search)
            # фильтрация объектов по пользователю
            # track = models.Tracking.objects.filter(user=request.user)[0]
            # print(type(track), track)
            # print(type(track.tracks), track.tracks)  # .all()
            # print(type(track.tracks.all()), track.tracks.all())
            # print(type(track.tracks.all().count()), track.tracks.all().count())
            # print(type(track.tracks.all().contains(item)), track.tracks.all().contains(item))
            # print(type(track.tracks.all().filter(track__contains="9262").delete()), track.tracks.all().filter(track__contains="9262"))

            return render(request, "django_app/track_find.html", {"item": item, "search": search})
        except Exception as error:
            print(error)
            return render(request, "django_app/track_find.html", {"item": None, "search": search, "error": "Трек код не совпадает"})


@custom_login_required
def track_add(request: HttpRequest, track: str) -> HttpResponse:
    """Добавление посылки в отслеживаемые для пользователя."""

    # 0. Переход Ваш сайт
    # 1. Его никуда, кроме цен, инструкций.. не пускает
    # 2. Он создаёт аккаунт и входит
    # 3. Переходит на страницу "поиск посылки"
    # 4. Вводит в строке поиска трек код от поставщика/продавца/системы...
    # 5. Если трек совпадает, ему выпадает инфа о посылке и возможность "прикрепить"
    # посылку к своему профилю
    # 6.
    # N. Посылать уведомления на профиль (телега/смс/письмо/вывод уведомления)

    user: User = request.user
    track_obj = models.Item.objects.get(track=track)

    # User +O2M+ Middle Model.py +M2M+ Item(Items)

    # track = models.Tracking.objects.create(user=user)
    # track.tracks.add(track_obj)
    # track.save()

    # защита от "задвоения"

    from django.core.exceptions import ObjectDoesNotExist

    # 1.
    # try:
    #     track = models.Tracking.objects.get(user=user)
    # except ObjectDoesNotExist:
    #     track = models.Tracking.objects.create(user=user)

    # 2.
    # track = models.Tracking.objects.objects.get_or_create(user=user)

    # 3.
    track = models.Tracking.objects.filter(user=user)
    if len(track) > 0:
        track = track[0]
    else:
        track = models.Tracking.objects.create(user=user)
    track.tracks.add(track_obj)  # set - unique
    track.save()

    # HTML -> VIEW
    # 1. HTML FORM
    # 2. <str:track> - dynamic parameter

    return redirect(reverse("track_list"))


@custom_login_required
def track_list(request: HttpRequest) -> HttpResponse:
    """Посылки пользователя для отслеживания."""

    """
    Показывает все посылки которые прикреплены к этому аккаунту
    """

    user: User = request.user
    track = models.Tracking.objects.filter(user=user)
    if len(track) > 0:
        data = track[0].tracks.all()
    else:
        data = []

    selected_page = request.GET.get(key="page", default=1)  # query parameter
    paginator = Paginator(data, 1)
    current_page = paginator.get_page(selected_page)

    # current_page = utils.CustomPaginator.paginate(object_list=data, limit=2, request=request)
    return render(request, "django_app/track_list.html", context={"current_page": current_page})


@custom_login_required
def track_update(request, track: str):  # запускает менеджер, когда обновляет выбранный товар
    # http://127.0.0.1:8000/track/update/NL-7217-6944-AZJ/
    """
    Нужно, чтобы при обновлении статуса на "доставлено" всем
    пользователя с этой посылкой отправлялись письма.

    """
    item_obj = models.Item.objects.get(track=track)
    # tracks_obj = models.Tracking.objects.all().contains(item_obj)
    tracks_obj = models.Tracking.objects.all()  # TODO нужно доработать
    # email = [i.user.email for i in tracks_obj if i.tracks.contains(item_obj)]
    emails_list = []
    for i in tracks_obj:
        if i.tracks.contains(item_obj):
            emails_list.append(i.user.email)

    def check_email(email_str: str):
        if re.match(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email_str):
            return True
        return False

    emails = list(filter(check_email, emails_list))  # regex
    print(emails)
    return HttpResponse(f"send_mail('Посылка доставлена', '...', {', '.join(emails)})")


# track = models.Tracking.objects.filter(user=request.user)[0]
# print(type(track), track)
# print(type(track.tracks), track.tracks)  # .all()
# print(type(track.tracks.all()), track.tracks.all())
# print(type(track.tracks.all().count()), track.tracks.all().count())
# print(type(track.tracks.all().contains(item)), track.tracks.all().contains(item))
# print(type(track.tracks.all().filter(track__contains="9262").delete()), track.tracks.all().filter(track__contains="9262"))
