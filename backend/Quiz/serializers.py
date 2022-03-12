from dataclasses import fields
from unicodedata import name
from wsgiref.validate import validator
from rest_framework import serializers
from Quiz.models.Category_model import Category
from Quiz.models.Quiz_model import Quiz
from Quiz.models.Question_model import Question
from Quiz.models.Options_model import Options


class CategorySerializers(serializers.ModelSerializer):
    quizzes = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'quizzes', 'cover', 'position']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


# class QuizSerializers(serializers.ModelSerializer):
#     quiz = serializers.StringRelatedField(many=True)
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'slug', 'quiz', 'cover', 'position']
#         lookup_field = 'slug'
#         extra_kwargs = {
#             'url': {'lookup_field': 'slug'}
#         }