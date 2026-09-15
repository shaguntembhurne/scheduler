from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('focus/<int:task_id>/', views.focus_view, name='focus_timer'),
    path('save_time/<int:task_id>/', views.save_time_view, name='save_time'),
]