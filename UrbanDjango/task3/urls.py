from django.urls import path
from . import views


app_name = 'task3'
urlpatterns = [
    path('platform/', views.platform_view, name='platform'),
    path('platform/games/', views.games_view, name='games'),
    path('platform/cart/', views.cart_view, name='cart'),
]

