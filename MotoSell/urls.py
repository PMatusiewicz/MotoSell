from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rejestracja', views.rejestracja, name='rejestracja'),
    path('login', views.login, name='login'),
    path('wyloguj', views.wyloguj, name='wyloguj'),
    path('pojazdy/kreator', views.kreator, name='kreator'),
    path('pojazdy', views.pojazdy, name='pojazdy'),
    path('pojazdy/moje/', views.moje_pojazdy, name='moje_pojazdy'),
    path('pojazdy/<int:pk>', views.oferta, name='oferta'),
    path('pojazdy/<int:pk>/publikuj', views.publikuj, name='publikuj'),
    path('pojazdy/<int:pk>/cofnij_publikacje', views.cofnij_publikacje, name='cofnij_publikacje'),
    path('pojazdy/<int:pk>/usun', views.usun, name='usun'),
    path('pojazdy/<int:pk>/edytuj', views.edytuj, name='edytuj'),
]
