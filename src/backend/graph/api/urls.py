from django.urls import path

from graph.api import views

urlpatterns = [
    path('', views.GraphList.as_view(), name='graph-list'),
    path('<int:pk>', views.GraphDetail.as_view(), name='graph-list'),
    path('create/', views.GraphCreate.as_view(), name='graph-list'),
    path('get_graphs/', views.get_graphs, name='get_graphs'),
]