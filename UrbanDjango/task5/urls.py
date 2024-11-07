from django.urls import path
from . import views


app_name = 'task5'
urlpatterns = [
    path('html_sign_up', views.sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up', views.sign_up_by_django, name='sign_up_by_django'),
]
