from django.urls import path, include
from .views import CategoryViewSet, QuizView, QuizDetailView, HomePage
from rest_framework_nested import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, basename='category')

categories_router = routers.NestedSimpleRouter(
    router, r'categories', lookup='category')
categories_router.register(r'quizzes', QuizView, basename='quizzes')

router.register(r'quiz', QuizDetailView, basename='quiz')
router.register(r'', HomePage, basename='home')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(categories_router.urls)),
]
