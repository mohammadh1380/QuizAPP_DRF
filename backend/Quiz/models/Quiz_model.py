from django.db import models
from Quiz.models.Category_model import Category
from .validators import validate_file_extension
from .managers import QuizManager

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    desc = models.CharField(max_length=500)    
    cover = models.FileField(upload_to="QuizCover", blank=True, null=True, validators=[validate_file_extension])
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Duration of the quiz in seconds", default="60")
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()
    
    objects = QuizManager()