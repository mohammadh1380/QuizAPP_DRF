from django.db import models
from .Quiz_model import Quiz
from .validators import validate_file_extension


class Question(models.Model):
    content = models.CharField(max_length=200)
    cover = models.FileField(upload_to="questionCover", blank=True, null=True, validators=[validate_file_extension]) # if a question have image
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
    def options(self):
        return self.options_set.all()
