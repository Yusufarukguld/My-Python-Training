class Question:
    def __init__(self,text,choices,correct):
        self.text = text
        self.choices = choices
        self.correct = correct

    
    def check_answer(self,answer):
        if answer not in self.choices:
            raise ValueError("Inappropriate")
        return answer == self.correct
 
import random
class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions,len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("Response:")
        if (question.check_answer(answer)):
            self.score += 1        

        self.questionIndex += 1
        self.loadquestion()
    
    def loadquestion(self):

        if (len(self.questions) == self.questionIndex):
            self.displayScore()
        else: 
            self.displayProgress()   
            self.displayQuestion()

    def displayScore(self):
        print("Quiz Summary".center(100,"*"))
        grade = 100 / (len(self.questions))
        Totalgrade = round(self.score * grade)
        print(f"You achieved {self.score} out of {len(self.questions)} questions")
        print("Grade:",Totalgrade)
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        print(f"You are in {questionNumber}. question out of {totalQuestion} questions ".center(100," "))
        
q1 = Question("what is the best programming language", ["python","java","C","C++"], "python")
q2 = Question("What is the most popular programming language", ["python","java","C","C++"], "python")
q3 = Question("what is the most profit-maker programming language", ["python","java","C","C++"], "python")

questions = [q1,q2,q3]


quiz = Quiz(questions) 

print(quiz.loadquestion())

