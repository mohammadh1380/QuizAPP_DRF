from django.db import models
from .Question_model import Question


class Options(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.correct:
            check = Options.objects.filter(question=self.question)
            for i in check:
                if i.correct:
                    self.correct = False
                    super(Options, self).save(*args, **kwargs)

        super(Options, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Options"

    def __str__(self):
        return self.content
