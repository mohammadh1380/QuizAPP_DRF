from django.db import models


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    cover = models.FileField(upload_to="categoryCover", blank=True, null=True, validators=[validate_file_extension])
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    def __str__(self):
        return self.name

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    desc = models.CharField(max_length=500)    
    cover = models.FileField(upload_to="QuizCover", blank=True, null=True, validators=[validate_file_extension])
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Duration of the quiz in seconds", default="60")
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quiz")

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()
    

class Question(models.Model):
    content = models.CharField(max_length=200)
    cover = models.FileField(upload_to="questionCover", blank=True, null=True, validators=[validate_file_extension]) # if a question have image
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
    def get_answers(self):
        return self.options_set.all()
        

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
