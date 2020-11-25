from django.urls import path
from .views import Home, Detail, Create

urlpatterns = [
    path('', Home.as_view(), name = "home"),
    path('article/<int:pk>', Detail.as_view(), name = "detail"),
    path('new/', Create.as_view(), name = "create"),
]
