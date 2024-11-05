from django.shortcuts import render

def platform_view (request):
    return render(request, 'third_task/platform.html')

def games_view(request):
    context = {
        'items': {
            'Atomic Heart': 'Купить',
            'Cyberpunk 2077': 'Купить',
            'PayDay 2': 'Купить'
        }
    }
    return render(request, 'third_task/games.html', context)

def cart_view(request):
    return render(request, 'third_task/cart.html')
