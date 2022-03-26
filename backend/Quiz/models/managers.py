from django.db import models


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)


class QuizManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

    def category_slug(self, category):
        return self.get_queryset().filter(category__slug=category)

    def quiz_slug(self, slug):
        return self.get_queryset().filter(slug=slug, status=True, category__status=True)
