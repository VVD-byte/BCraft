from django.urls import path
from api import views


urlpatterns = [
    path('statistics/create', views.CreateStatisticView.as_view(), name='CreateCreate'),
    path('statistics/list', views.ListStatisticView.as_view(), name='ListCreate'),
    path('statistics/drop', views.DropStatisticView.as_view(), name='DropCreate'),
]
