from Quiz.models.Category_model import Category
from Quiz.models.Quiz_model import Quiz
from Quiz.models.Question_model import Question
from Quiz.models.Options_model import Options
from django.test import TestCase


class ModelsTest(TestCase):

    def setUp(self):
        Category.objects.create(name="Game", slug="game", status=False, position=2)
        Quiz.objects.create(name="Clash", slug="clash", desc="a army game", number_of_questions=2, time=120, status=True, category=Category.objects.get(name="Game"))
        Question.objects.create(content="number of towns ?", quiz=Quiz.objects.get(name="Clash"))
        Options.objects.create(content="12", correct=True, question=Question.objects.get(content="number of towns ?"))
        

    def test_category(self):
        game = Category.objects.get(name="Game")

        self.assertEqual(game.name, 'Game')
        self.assertEqual(game.slug, "game")
        self.assertEqual(game.position, 2)
        self.assertFalse(game.status)

    def test_quiz(self):
        game = Category.objects.get(name="Game")
        clash = Quiz.objects.get(name="Clash")
        self.assertEqual(clash.name, 'Clash')
        self.assertEqual(clash.slug, "clash")
        self.assertEqual(clash.number_of_questions, 2)
        self.assertTrue(clash.status)
        self.assertEqual(clash.category, game)
        self.assertQuerysetEqual(clash.get_questions(), ["<Question: number of towns ?>",])


    def test_question(self):
        game = Category.objects.get(name="Game")
        clash = Quiz.objects.get(name="Clash")
        ques = Question.objects.get(content="number of towns ?")
        
        self.assertEqual(ques.content, "number of towns ?")
        self.assertEqual(ques.quiz, clash)
        self.assertQuerysetEqual(ques.get_answers(), ["<Options: 12>"])


    def test_options(self):
        game = Category.objects.get(name="Game")
        clash = Quiz.objects.get(name="Clash")
        ques = Question.objects.get(content="number of towns ?")
        option = Options.objects.get(content="12")

        self.assertEqual(option.content, "12")
        self.assertTrue(option.correct)
        self.assertEqual(option.question, ques)
        
        