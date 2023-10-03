import datetime
import re
import sqlite3
from django.db import connection
from django.http import HttpRequest, HttpResponse  # native django
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from django_app import models, serializers


def index(request):
    return render(request, "index.html")


@api_view(http_method_names=["GET", "POST"])
# @permission_classes([AllowAny])
# @csrf_exempt
def resume(request: Request) -> Response:
    try:
        if request.method == "GET":
            # filter - фильтрация, т.е. выбор нужных данных
            # search - поиск, т.е. выбор нужных данных
            # order - сортировка, т.е. порядок отображения
            # cache - использование старых данных, для ускорения
            # пагинация - разделение данных на порции(страницы), для ускорения

            # http://127.0.0.1:8000/resume/?search=Бо

            search = str(request.GET.get("search", ""))

            # resume_s = models.Resume.objects.all()
            resume_s = models.Resume.objects.filter(first_name__icontains=search)
            resume_json = serializers.ResumeSerializer(resume_s, many=True).data

            # native serialization
            # data = []
            # for i in resume_s:
            #     data.append(
            #         {
            #             "id": i.id,
            #             "first_name": i.first_name,
            #         }
            #     )

            return Response({"list": resume_json}, status=status.HTTP_200_OK)
        elif request.method == "POST":
            # {"first_name": "John"} False
            # {"first_name": "богдан"}  False
            # {"first_name": "Богдан"} False
            # {"first_name": "Богдан123"} True
            first_name = request.data["first_name"]
            # validation == кириллица, минимум 1 цифра, и оба регистра, минимум 4
            # first_name.lower()
            # first_name.upper()
            # first_name.isascii()
            # first_name.isalpha()
            if re.match(r"^(?=.*?[а-я])(?=.*?[А-Я])(?=.*?[0-9]).{4,}$", first_name) is None:
                return Response(data={"message": "Validation Error!"}, status=status.HTTP_400_BAD_REQUEST)
            r1 = models.Resume.objects.create(first_name=first_name)
            return Response({"message": f"Успешно! ({r1.id})"}, status=status.HTTP_201_CREATED)
    except Exception as error:
        return Response(data={"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)


def register_mvt(request: HttpRequest, pk=0) -> HttpResponse:
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        try:
            print("POST")
            print(pk)  # dynamic parameter https://www.olx.kz/prokat-tovarov/instrumenty-i-oborudovanie/
            print(request.GET)  # query_params  https://hh.ru/search/vacancy?text=Python&area=154
            print(request.POST)  # форма in MVT
            form = request.POST
            first_name = form["first_name"]  # unsafe (Exception(KeyError))
            date: datetime.datetime | None = form.get("date", None)  # safe
            print(request.FILES)  # файлы
            # print(request.body)  # form in bytes
            # print(request.data)  # JSON for DRF
            print(first_name, date)

            # RAW SQL
            #         with sqlite3.Connection("db.sqlite3") as connection:
            #             cursor = connection.cursor()
            #             query = """
            # INSERT INTO resume_model_table (first_name, date)
            # VALUES (?, ?)
            # """
            #             cursor.execute(query, (first_name, date))
            #             connection.commit()

            # DJANGO RAW
            #         cursor = connection.cursor()  #
            #         query = """
            # INSERT INTO resume_model_table (first_name, date)
            # VALUES (%s, %s)
            # """
            #         cursor.execute(query, (first_name, date))
            #         connection.commit()

            # ORM
            r1 = models.Resume.objects.create(first_name=first_name, date=date)
            if r1.id % 2 == 0:
                # r1.delete()
                # raise KeyError()
                raise Exception("ID чётный!")

            query = """
            -- select max(id) from resume_model_table
            select id from resume_model_table WHERE time = (MAX(time) from resume_model_table)
            """

            return render(request, "register.html", {"success": "Успешно!"})
        # except KeyError as error:
        #     pass
        except Exception as error:
            return render(request, "register.html", {"error": str(error)})


# todo ООП: Наследование #########################################################
class Worker:
    def get_salary(self):
        print("Хочу зарплату!")


class Buh(Worker):
    def get_salary(self):
        print("Даёт зарплату")


class Sys(Worker):
    pass


class Designer(Worker):
    pass


# s1 = Sys()
# s1.get_salary()
# todo ООП: Наследование #########################################################


if __name__ == "__main__":
    #     with sqlite3.Connection("../db.sqlite3") as connection:
    #         cursor = connection.cursor()
    #         query = """
    # select * from resume_model_table;
    # """
    #         cursor.execute(query)
    #         rows = cursor.fetchall()
    #         for i in rows:
    #             print(i)
    pass
