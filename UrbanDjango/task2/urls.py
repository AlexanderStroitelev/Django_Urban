from django.urls import path
from . import views

urlpatterns = [
    path('function-view/', views.function_view),
    path('class-view/', views.ClassView.as_view()),
]