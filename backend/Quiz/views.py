from rest_framework import viewsets  
from .models.Category_model import Category
from .models.Quiz_model import Quiz
from .models.Question_model import Question
from .models.Options_model import Options
from .permissions import IsSuperuserOrReadOnly
from .serializers import CategorySerializers

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.active()
    serializer_class = CategorySerializers
    permission_classes = [IsSuperuserOrReadOnly, ]
    lookup_field = 'slug'

# class QuizViewSet(viewsets.ModelViewSet):
#     queryset = 