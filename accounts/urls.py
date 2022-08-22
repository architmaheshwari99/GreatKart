from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("activate/<uidb>/<token>/", views.activate, name="activate"),
    path("forgotPassword/", views.forgotPassword, name="forgotPassword"),
    path("resetPassword/", views.resetPassword, name="resetPassword"),
    path("", views.dashboard, name="dashboard"),
    path("resetpassword_validate/<uidb>/<token>/", views.resetpassword_validate, name="resetpassword_validate"),
]
