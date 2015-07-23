from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the cards index.")

def detail(request, card_id):
    return HttpResponse("You're looking at card %s." % card_id)
