from django.views.generic import TemplateView


class PlatformView(TemplateView):
    template_name = 'fourth_task/platform1.html'

class GamesView(TemplateView):
    template_name = 'fourth_task/games1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games1'] = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
        context [ 'purchase_link' ] = 'Купить'
        return context

class CartView(TemplateView):
    template_name = 'fourth_task/cart1.html'