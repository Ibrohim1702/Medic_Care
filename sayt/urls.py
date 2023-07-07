from django.urls import path

from sayt.views import *

urlpatterns = [
    path("", index, name="home"),
]