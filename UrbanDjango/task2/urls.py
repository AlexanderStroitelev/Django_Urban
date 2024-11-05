from django.urls import path
from . import views

app_name = 'task2'
urlpatterns = [
    path('function-view/', views.function_view),
    path('class-view/', views.ClassView.as_view()),
]