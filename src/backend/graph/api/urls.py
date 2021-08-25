from django.urls import path

from .views import get_graphs

urlpatterns = [
    path('', get_graphs, name='get_graphs'),
]