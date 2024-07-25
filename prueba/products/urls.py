from django.urls import path
from .views import ProductoList, ProductoDetail

urlpatterns = [
    path('', ProductoList.as_view(), name='producto-list'),
    path('<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
]