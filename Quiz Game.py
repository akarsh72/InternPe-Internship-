                                ###   Quiz Game   ###

class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def check_answer(self, user_answer):
        return user_answer == self.correct_choice


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def take_quiz(self):
        for question in self.questions:
            print(question.text)
            for i, choice in enumerate(question.choices, start=1):
                print(f"{i}. {choice}")
            
            user_answer = input("Enter the number of your choice: ")
            
            try:
                user_answer = int(user_answer)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if 1 <= user_answer <= len(question.choices):
                user_answer -= 1  
                if question.check_answer(user_answer):
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Sorry, the correct answer is {question.choices[question.correct_choice]}\n")
            else:
                print("Invalid choice. Please select a valid option.\n")
        
        print(f"Quiz complete! Your score is {self.score}/{len(self.questions)}.")


questions = [
    Question("What is the capital of France?", ["Paris", "London", "Berlin"], 0),
    Question("What is the largest planet in our solar system?", ["Mars", "Jupiter", "Earth"], 1),
    Question("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Carbon dioxide", "Nitrogen"], 1),
]

quiz = Quiz(questions)
quiz.take_quiz()
