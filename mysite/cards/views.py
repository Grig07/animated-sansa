from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Card
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_card_list = Card.objects.order_by('-created_at')[:20]
    template = loader.get_template('cards/index.html')
    context = RequestContext(request, {
        'latest_card_list': latest_card_list,
    })
    return HttpResponse(template.render(context))


def details(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/details.html', {'card': card})