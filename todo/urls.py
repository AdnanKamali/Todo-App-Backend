from django.urls import path

from .views import user_view

urlpatterns = [
    path("register/", user_view.SignUpViewImpl.as_view(), name="register"),
    path("information/", user_view.SignUpInformationViewImpl.as_view(), name="information"),
]