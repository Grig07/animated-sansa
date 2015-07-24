from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Card
from django.shortcuts import get_object_or_404, render


def index(request):
    lastest_cards_list = Card.objects.order_by('-created_at')[:20]
    template = loader.get_template('cards/index.html')
    context = RequestContext(request, {
        'lastest_cards_list': lastest_cards_list,
    })
    return HttpResponse(template.render(context))


def detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/detail.html', {'card': card})