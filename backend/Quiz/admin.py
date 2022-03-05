from unicodedata import category
from django.contrib import admin
from .models import Category, Options, Question, Quiz

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'slug')
    prepopulated_fields = {"slug": ("name",)}


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'slug', 'category_to_str', 'status')
    prepopulated_fields = {"slug": ("name",)}


    def category_to_str(self, obj):
        return obj.category.name

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'quiz')
     
    def quiz_to_str(self, obj):
        return obj.quiz.name

   
class OptionsAdmin(admin.ModelAdmin):
    list_display = ('content', 'question', 'correct')
     
    def quiz_to_str(self, obj):
        return obj.question.name 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Options, OptionsAdmin)