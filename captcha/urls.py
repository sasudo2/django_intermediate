from django.urls import path
from . import views

app_name = "captcha"

urlpatterns = [
    path("", views.index, name = "index"),
]