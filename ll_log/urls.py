from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'll_log'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topic, name='topic'),
    path('add_topic/', views.add_topic, name='add_topic'),
    path('topics/<int:topic_id>/', views.entry, name='entry'),
    path('topics/<int:topic_id>/entry/<int:entry_id>/', views.nest, name='nest'),
    path('topics/<int:topic_id>/new_entry/', views.new_entry, name='new_entry'),
    path('topics/<int:topic_id>/entry/<int:entry_id>/new/', views.new_nest, name='new_nest'),
    path('edit/<int:nest_id>/', views.edit, name='edit'),
    # Add more paths as needed for your views
]
