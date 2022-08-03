from django.urls import path
from .views import *

app_name = "furn"

urlpatterns = [
    path('',home, name="home"),
    path("<int:pk>/detalis/", arrivals_detail, name="arrivals_detal"),
    path("signup/", signup, name="signup")
]
