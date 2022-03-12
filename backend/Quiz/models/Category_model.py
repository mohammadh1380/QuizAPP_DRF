from django.db import models
from .validators import validate_file_extension
from .managers import CategoryManager

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    cover = models.FileField(upload_to="categoryCover", blank=True, null=True, validators=[validate_file_extension])
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    def __str__(self):
        return self.name
    
    def quizzes(self):
        return self.quiz_set.active()

    objects = CategoryManager()