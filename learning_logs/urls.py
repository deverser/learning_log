"""Определяет схемы URL для learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Вывод всех тем
    path('topics/', views.topics, name='topics'),
    # Подробная страница одной темы
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]