from django.contrib import admin
from .models.Category_model import Category
from .models.Quiz_model import Quiz
from .models.Question_model import Question
from .models.Options_model import Options


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'slug', 'status')
    prepopulated_fields = {"slug": ("name",)}


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'slug', 'category', 'status')
    prepopulated_fields = {"slug": ("name",)}

    def category(self, obj):
        return obj.category.name


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'quiz')


class OptionsAdmin(admin.ModelAdmin):
    list_display = ('content', 'question', 'correct')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Options, OptionsAdmin)
