from django.db import models

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
    

class QuizManager(models.Manager):
    def active(self):
        return self.filter(status=True)