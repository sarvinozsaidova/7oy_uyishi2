from django.urls import path
from . import views

urlpatterns = [
    path('avtos/', views.avtos, name='avtos'),
    path('avto/<str:pk>', views.avto, name='avto'),
    path('avtodelete/<str:pk>', views.avtodelete, name='avtodelete'),
    path('avtoupdate/<str:pk>', views.avtoupdate, name='avtoupdate'),
]