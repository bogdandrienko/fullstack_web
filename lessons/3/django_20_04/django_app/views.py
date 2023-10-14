from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from django_app import models, serializers


@csrf_exempt  # - отключает защиту csrf для этого контроллера (POST)
def api_native(request: HttpRequest) -> JsonResponse:
    return JsonResponse(data={"message": "OK"}, safe=True)


@api_view(http_method_names=["GET", "POST"])
def api_drf(request: Request, pk: str, category: str) -> Response:
    # http://127.0.0.1:8000/api/drf/666/777?search=dog&page=12
    # {"fio": "Богдан А.", "iin": 970801}
    print("dynamic parameter: ", pk, category)  # dynamic parameter path("api/drf/<str:pk>/<str:category>")
    print("query parameter: ", request.GET)  # query params http://127.0.0.1:8000/api/drf/666/777?search=dog&page=12
    print(request.POST)  # encoding=multipart-form-data
    print(request.FILES)  # files
    print("JSON data: ", request.data)  # dictionary JSON

    return Response(data={"message": "OK"}, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
def worker(request: Request, pk: str = "-1") -> Response:
    if pk == "-1":
        if request.method == "GET":
            # GET(many)
            _workers_obj = models.Worker.objects.all()  # ORM
            print(_workers_obj)  # <QuerySet []> | <QuerySet [<Worker: <Worker 970801 Богдан Андриенко>>]>
            _workers_json = serializers.WorkerSerializer(_workers_obj, many=True).data
            return Response(data={"data": _workers_json}, status=status.HTTP_200_OK)
        elif request.method == "POST":
            # {"iin": 777, "first_name": "Имя", "last_name": "Фамилия"}
            # request.data
            form = request.data
            iin = form.get("iin", None)  # safe
            if iin is None:
                raise Exception("Нету ИИН-а")

            first_name = form["first_name"].strip()  # unsafe == Exception
            last_name = form["last_name"].strip()  # unsafe == Exception

            _worker = models.Worker.objects.create(
                iin=iin,
                first_name=first_name,
                last_name=last_name,
            )

            return Response(data={"message": f"successfully {_worker.id}"}, status=status.HTTP_201_CREATED)
    else:
        if request.method == "GET":
            _worker_obj = models.Worker.objects.get(id=int(pk))
            _worker_json = serializers.WorkerSerializer(_worker_obj, many=False).data
            return Response(data={"data": _worker_json}, status=status.HTTP_200_OK)
        elif request.method == "PUT":
            # http://127.0.0.1:8000/api/worker/1/
            # {"first_name": "БОГДАН"}
            _worker_obj = models.Worker.objects.get(id=int(pk))
            if request.data.get("iin", None):
                _worker_obj.iin = request.data["iin"]
            if request.data.get("first_name", None) and _worker_obj.first_name != request.data["first_name"]:
                _worker_obj.first_name = request.data["first_name"]
            if request.data.get("last_name", None):
                _worker_obj.last_name = request.data["last_name"]
            _worker_obj.save()
            return Response(data={"message": "updated"}, status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            models.Worker.objects.get(id=int(pk)).delete()
            return Response(data={"message": "deleted"}, status=status.HTTP_200_OK)

