from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models.Category_model import Category
from .models.Quiz_model import Quiz
from .models.Question_model import Question
from .models.Options_model import Options
from .permissions import IsSuperuserOrReadOnly
from .serializers import CategorySerializers, QuizSerializers


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.active()
    serializer_class = CategorySerializers
    permission_classes = [IsSuperuserOrReadOnly, ]
    lookup_field = 'slug'


class QuizViewSet(viewsets.ModelViewSet):
    def get_queryset(self, **kwargs):
        print(self.kwargs.get('category_slug'))
        return Quiz.objects.categorySlug(self.kwargs.get('category_slug'))

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    serializer_class = QuizSerializers
    permission_classes = [IsSuperuserOrReadOnly, ]
    lookup_field = 'slug'
