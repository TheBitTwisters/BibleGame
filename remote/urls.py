from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('buzz/', views.buzz, name='buzz'),
]
