from .models.Category_model import Category
from .models.Quiz_model import Quiz
from .permissions import IsSuperuserOrReadOnly
from .serializers import CategorySerializers, QuizListSerializers, QuizDetailSerializers
from rest_framework import viewsets, mixins


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.active_objects
    serializer_class = CategorySerializers
    permission_classes = [IsSuperuserOrReadOnly, ]
    lookup_field = 'slug'


class QuizView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    def get_queryset(self, **kwargs):
        return Quiz.active_objects.category_slug(self.kwargs.get('category_slug'))

    serializer_class = QuizListSerializers
    permission_classes = [IsSuperuserOrReadOnly, ]


class QuizDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    def get_queryset(self, **kwargs):
        return Quiz.active_objects.quiz_slug(self.kwargs.get('slug'))

    serializer_class = QuizDetailSerializers
    permission_classes = [IsSuperuserOrReadOnly, ]
    lookup_field = 'slug'
