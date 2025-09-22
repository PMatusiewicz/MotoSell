from django.urls import path, include
from . import views_api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pojazdy', views_api.PojazdViewSet, basename='pojazd')

urlpatterns = [
    path('', include(router.urls)),
]