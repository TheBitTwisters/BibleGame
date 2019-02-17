from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('play/', views.play, name='play'),
    path('view/', views.view, name='view'),
    path('question/', views.question, name='question'),
    path('choice/', views.choice, name='choice'),
    path('fails/', views.fails, name='fails'),
    path('team_score/', views.team_score, name='team_score'),
    path('timer/', views.timer, name='timer'),
    path('event/', views.event, name='event')
]
