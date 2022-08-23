# pages/urls.py
from django.urls import path
from .views import homePageView, checkoutSessionView

urlpatterns = [
    path("", homePageView, name="home"),
    path("checkoutsession/", checkoutSessionView, name="checkoutsession"),
]
