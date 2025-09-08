from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rejestracja', views.rejestracja, name='rejestracja'),
    path('login', views.login, name='login'),
    path('wyloguj', views.wyloguj, name='wyloguj'),
    path('pojazdy/kreator', views.kreator, name='kreator')
]
