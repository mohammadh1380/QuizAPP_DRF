from rest_framework.test import APITestCase, APIClient
from django.test import Client
from django.urls import reverse
from rest_framework import status
from ..models.Category_model import Category
from ..serializers import CategorySerializers

# client = APIClient()
#
#
# class TestViews(APITestCase):
#     def setUp(self):
#         Category.objects.create(name="Game", slug="game", status=False, position=6)
#
#     def test_view_set(self):
#         cat = Category.objects.get(name='Game')
#         serializer = CategorySerializers(cat)
#         response = client.get('/categories/game/')
#         print(response.data)
#         print(response.status_code)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
