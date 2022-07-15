from django.urls import path
from dashboard.views import  *

app_name = "app"

urlpatterns = [
    path('', Home.as_view(), name="adminHome"),
    path('btns/', Btns.as_view(), name="adminBtns"),
    path('cards/', Cards.as_view(), name="adminCards"),
    path('blank/', Blank.as_view(), name="blank"),
    path('colors/', Colors.as_view(), name="colors"),
    path('borders/', Borders.as_view(), name="borders"),
    path('animations/', Animations.as_view(), name="animations" ), 
    path('others/', Others.as_view(), name="others")
]
