from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("activate/<uidb>/<token>/", views.activate, name="activate"),
]
