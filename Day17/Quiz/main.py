from question_model import  Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

#quiz.end_game()
print("You've Completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.q_no}")