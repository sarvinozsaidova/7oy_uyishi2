from django.urls import path
# from . import views
from .views import AvtoListView, AvtoDetailView, AvtoDeleteView, AvtoCreateView, AvtoUpdateView

urlpatterns = [
    path('avtos/', AvtoListView.as_view(), name='avtos'),
    path('avto/<str:pk>', AvtoDetailView.as_view(), name='avto'),
    path('avto/delete/<str:pk>', AvtoDeleteView.as_view(), name='avto'),
    path('avto/create/', AvtoCreateView.as_view(), name='avtocreate'),
    path('avto/update/<str:pk>', AvtoUpdateView.as_view(), name='avto'),
    # path('avto/<str:pk>', views.avto, name='avto'),
    # path('avtodelete/<str:pk>', views.avtodelete, name='avtodelete'),
    # path('avtoupdate/<str:pk>', views.avtoupdate, name='avtoupdate'),
]