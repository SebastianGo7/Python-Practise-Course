from typing import List

from quiz_brain import QuizBrain
from question_model import Question
from data import question_data


# Creating a question bank from data file
question_bank: list[Question] = []
for question in range (0, len(question_data)):
   question_bank.append(Question(question_data[question]["question"], question_data[question]["correct_answer"]))



quiz = QuizBrain(question_bank)


while quiz.still_has_questions():

    quiz.check_answer(quiz.next_question())

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")

