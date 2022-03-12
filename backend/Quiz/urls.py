from django.urls import path, include
from .views import CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = DefaultRouter()
router.register(r'', CategoryViewSet, basename='category')
urlpatterns = router.urls



# router = routers.SimpleRouter(trailing_slash=False)
# router.register(r'categories', CategoryViewSet)

# categories_router = routers.NestedSimpleRouter(
#     router, r'categories', lookup='category', trailing_slash=False)
# categories_router.register(r'items', ItemViewSet)