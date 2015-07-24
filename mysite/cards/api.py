from rest_framework import serializers, viewsets
from .models import Card


class CardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Card
		


class CardViewSet(viewsets.ModelViewSet):
	queryset = Card.objects.all()
	serializer_class = CardSerializer	
