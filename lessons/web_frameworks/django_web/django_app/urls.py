from django.urls import path, re_path
from django_app import views

# from django_app.views import home, index, ...

urlpatterns = [
    path("get_string/", views.get_string),
    path("get_html_string/", views.get_html_string),
    path("get_json/", views.get_json),
    path("get_html_file/", views.get_html_file),
    path("get_dynamic/", views.get_dynamic),  #  != /get_dynamic
    path("get_dynamic/<str:ml>/", views.get_dynamic),
    path("get_args/", views.get_args),
    path("get_html_form/", views.get_html_form, name="get_html_form"),
    # re_path(r"^users/(?P<pk>\d+)/detail/$", views.todo_f, name="todo_pk"),
]
