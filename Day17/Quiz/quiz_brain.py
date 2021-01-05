class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.q_no = 0
        self.score=0

    def still_has_question(self):
        if self.q_no in range(0, len(self.q_list)):
            return True
        else:
            return False

    def next_question(self):
        cur_ques = self.q_list[self.q_no]
        self.q_no += 1
        ans = input(f"Q.{self.q_no}: {cur_ques.question} (True/False )")
        self.check_answer(ans,cur_ques.ans)
    def check_answer(self,usr_ans,cr_ans):
        if usr_ans.lower() == cr_ans.lower():
            print("You Got it right")
            self.score += 1
        else:
            print("That's Wrong")
        print(f"The right answer was {cr_ans}")
        print(f"The current Score is {self.score}/{self.q_no}")
        print("\n")
    def end_game(self):
        if self.q_no==12:
            print("You Have Completed the quiz ")
            print(f"Your Final Score was {self.score}/{self.q_no}")




