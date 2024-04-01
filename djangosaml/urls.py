from django.urls import path, include
from . import views

app_name = 'djangosaml'

urlpatterns = [
    path('acs/', views.acs, name="acs"),
    path('welcome/', views.welcome, name="welcome"),
    path('denied/', views.denied, name="denied"),
    path('login/', views.signin, name="login"),
]

