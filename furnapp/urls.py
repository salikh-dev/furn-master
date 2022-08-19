from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from .views import *

app_name = "furn"

urlpatterns = [
    path('',home, name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("<int:pk>/detalis/", arrivals_detail, name="arrivals_detal"),
    path("signup/", signup, name="signup"),
    path('profile/', Profileview.as_view(), name="profile"),
    path('edit_profile/', EditProfileView.as_view(), name="edit")
]
