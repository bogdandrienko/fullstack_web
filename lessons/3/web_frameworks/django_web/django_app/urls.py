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
    # tracking
    path("", views.home, name=""),
    path("home/", views.home, name="home"),
    path("login/", views.login_, name="login"),
    path("logout/", views.logout_, name="logout"),
    path("track/start/", views.track_start, name="track_start"),
    path("track/middle/", views.login_, name="track_middle"),
    path("track/end/", views.login_, name="track_end"),
    path("track/find/", views.track_find, name="track_find"),
    path("track/add/<str:track>/", views.track_add, name="track_add"),
    path("track/remove/<str:track>/", views.login_, name="track_remove"),
    path("track/list/", views.track_list, name="track_list"),
    path("track/update/<str:track>/", views.track_update, name="track_update"),
]
