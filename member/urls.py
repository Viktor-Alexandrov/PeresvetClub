from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('coach/', views.coach, name='coach'),
    path('schedule/', views.schedule, name='schedule'),
    path('news/', views.news, name='news'),
    path('archive/', views.archive, name='archive'),
]
