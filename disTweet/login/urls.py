from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("thanks/", views.thanks, name="thanks"),
    path("registration/", views.registeration, name="login"),
]