from django.urls import path

from my_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]