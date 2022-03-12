from rest_framework.test import APIRequestFactory
from django.test import TestCase
from Quiz.models.Category_model import Category
from Quiz.views import CategoryViewSet

# class TestViews(TestCase):
#     def setUp(self):
#         Category.objects.create(name="Game", slug="game", status=False, position=2)
#     def test_view_set(self):
#         request = APIRequestFactory().get("/game")
        
        # cat_detail = CategoryViewSet.as_view({'get': 'retrieve'})
        # cat = Category.objects.get(name="Game")
        # print(request)
        # response = cat_detail(request, slug=cat.slug)
        # self.assertEqual(response.status_code, 200)

