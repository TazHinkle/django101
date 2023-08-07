from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("taz", views.taz, name="taz"),
    path("<str:name>", views.greet, name="greet")
]
