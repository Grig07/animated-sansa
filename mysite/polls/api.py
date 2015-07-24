from rest_framework import serializers, viewsets
from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		field = ('url', 'id')

class QuestionSerializer(serializers.ModelSerializer):
	choice=ChoiceSerializer(many=True, read_only=True)

	class Meta:
		model = Question
		fields = ('url', 'id', 'pub_date', 'question_text', 'choice')


		

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer	

class ChoiceViewSet(viewsets.ModelViewSet):
	queryset = Choice.objects.all()
	serializer_class = ChoiceSerializer	