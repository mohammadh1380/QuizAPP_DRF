from rest_framework import serializers
from .models.Category_model import Category
from .models.Quiz_model import Quiz
from .models.Question_model import Question
from .models.Options_model import Options


class CategorySerializers(serializers.ModelSerializer):
    quizzes = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'quizzes', 'cover', 'position']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }