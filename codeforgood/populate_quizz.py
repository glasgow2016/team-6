import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeforgood.settings')
django.setup()

from brake_classroom.models import Question



def populate():
    print("Populating..")
    q1_level1 = Question(
        level='walking',
        number=1,
        question_title="question1",
        right_answer="Right",
        wrong_answer1="Wrong1",
        wrong_answer2="Wrong2",
        wrong_answer3="Wrong3"
    )
    q1_level1.save()

    q2_level1 = Question(
        level='walking',
        number=2,
        question_title="question2",
        right_answer="Right2",
        wrong_answer1="Wrong2",
        wrong_answer2="Wrong2.2",
        wrong_answer3="Wrong2.3"
    )
    q2_level1.save()
    q3_level1 = Question(
        level='walking',
        number=3,
        question_title="question3",
        right_answer="Right3.1",
        wrong_answer1="Wrong3.1",
        wrong_answer2="Wrong3.2",
        wrong_answer3="Wrong3.3"
    )
    q3_level1.save()
    q4_level1 = Question(
        level='walking',
        number=4,
        question_title="question4",
        right_answer="right4",
        wrong_answer1="wrong4.1",
        wrong_answer2="wrong4.2",
        wrong_answer3="wrong4.3"
    )
    q4_level1.save()
    q5_level1 = Question(
        level='walking',
        number=5,
        question_title="question5",
        wrong_answer1="wrong5.1",
        wrong_answer2="wrong5.2",
        wrong_answer3="wrong5.3"
    )
    q5_level1.save()


if __name__ == '__main__':
    print("Populating main")
    populate()
    print("Populated ")
