"""Определяет схемы URL для learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Страница для добавления нового сообщения
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Удаление записи
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    # Подробная страница одной темы
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Удаление темы
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    # Вывод всех тем
    path('topics/', views.topics, name='topics'),
    # Домашняя страница
    path('', views.index, name='index'),
]
