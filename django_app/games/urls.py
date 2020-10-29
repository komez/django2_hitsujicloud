from django.urls import path
from . import views
from django.contrib.auth import logout

app_name = 'games'
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', logout, name='logout'), 
]