from rest_framework import serializers
from .models.Category_model import Category
from .models.Quiz_model import Quiz
from .models.Question_model import Question
from .models.Options_model import Options


class CategorySerializers(serializers.ModelSerializer):
    quizzes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'quizzes', 'cover', 'position', 'status']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class OptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['content', 'correct']


class QuestionSerializers(serializers.ModelSerializer):
    options = OptionSerializers(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['content', 'cover', 'options']


class QuizListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'name', 'slug', 'desc', 'cover', 'number_of_questions', 'time', 'category', 'status']


class QuizDetailSerializers(serializers.ModelSerializer):
    questions = QuestionSerializers(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'slug', 'desc', 'cover', 'number_of_questions', 'time', 'questions']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

