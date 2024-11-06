from django.urls import path
from .views import PlatformView , GamesView , CartView


app_name = 'task4'
urlpatterns = [
    path('platform1/', PlatformView.as_view(), name='platform1'),
    path('platform1/games1/', GamesView.as_view(), name='games1'),
    path('platform1/cart1/', CartView.as_view(), name='cart1'),
]
