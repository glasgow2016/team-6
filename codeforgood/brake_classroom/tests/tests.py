from django.test import TestCase
from brake_classroom.models import Question


class QuestionModelTest(TestCase):

    def setUp(self):
        """
        Create fixture for the Question model
        """
        self.question1 = Question(
            level="walking",
            number="1",
            question_title="Is it a good idea to walk?",
            right_answer="Yes",
            wrong_answer1="No",
            wrong_answer2="No",
            wrong_answer3="No"
        )
        self.question1.save()

        self.question2 = Question(
            level="walking",
            number="2",
            question_title="Is it a good idea to run?",
            right_answer="Yes",
            wrong_answer1="No",
            wrong_answer2="No",
            wrong_answer3="No"
        )
        self.question2.save()

    def test_not_equal(self):
        self.assertNotEqual(self.question2, self.question1)
