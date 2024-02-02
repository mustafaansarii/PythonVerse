import random
class QuizGame:
    def __init__(self):
        self.questions = [
             {
                "question": "What is the capital of Japan?",
                "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
                "correct_answer": "Tokyo"
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["Oxygen", "Osmium", "Ozone", "Ochre"],
                "correct_answer": "Oxygen"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
                "correct_answer": "Leonardo da Vinci"
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1942", "1945", "1950", "1960"],
                "correct_answer": "1945"
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct_answer": "Blue Whale"
            },
            {
                "question": "Who wrote 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "J.K. Rowling", "George Orwell", "F. Scott Fitzgerald"],
                "correct_answer": "Harper Lee"
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "options": ["Earth", "Mars", "Venus", "Jupiter"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is the capital of Australia?",
                "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
                "correct_answer": "Canberra"
            },
            {
                "question": "What is the currency of Brazil?",
                "options": ["Dollar", "Euro", "Real", "Yen"],
                "correct_answer": "Real"
            },
            {
                "question": "Who wrote '1984'?",
                "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Arthur C. Clarke"],
                "correct_answer": "George Orwell"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "correct_answer": "Pacific Ocean"
            },
            {
                "question": "In which year did the Titanic sink?",
                "options": ["1912", "1920", "1930", "1940"],
                "correct_answer": "1912"
            },
            {
                "question": "Who painted 'Starry Night'?",
                "options": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Leonardo da Vinci"],
                "correct_answer": "Vincent van Gogh"
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["0", "1", "2", "3"],
                "correct_answer": "2"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "Vietnam"],
                "correct_answer": "Japan"
            },
            {
                "question": "Who is known as the 'Father of Computer Science'?",
                "options": ["Alan Turing", "Charles Babbage", "Ada Lovelace", "Bill Gates"],
                "correct_answer": "Alan Turing"
            },
            {
                "question": "What is the currency of Japan?",
                "options": ["Won", "Yuan", "Yen", "Ringgit"],
                "correct_answer": "Yen"
            },
            {
                "question": "Who wrote 'Pride and Prejudice'?",
                "options": ["Jane Austen", "Charlotte Brontë", "Emily Dickinson", "F. Scott Fitzgerald"],
                "correct_answer": "Jane Austen"
            },
            {
                "question": "In what year did the first moon landing occur?",
                "options": ["1965", "1969", "1973", "1980"],
                "correct_answer": "1969"
            }
        ]
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer the following questions and test your knowledge.")

    def display_question(self, question_data):
        print("\nQuestion:", question_data["question"])
        for i, option in enumerate(question_data["options"], start=1):
            print(f"{i}. {option}")

    def get_user_answer(self):
        while True:
            user_input = input("Enter your answer (1, 2, 3, or 4): ")
            if user_input.isdigit() and 1 <= int(user_input) <= 4:
                return int(user_input)
            else:
                print("Invalid input. Please enter a number between 1 and 4.")

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct! Well done!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")

    def play_game(self):
        self.display_welcome_message()

        while True:
            random.shuffle(self.questions)
            for question_data in self.questions:
                self.display_question(question_data)
                user_answer = self.get_user_answer()
                correct_index = question_data["options"].index(question_data["correct_answer"]) + 1
                self.evaluate_answer(user_answer, correct_index)

            print(f"\nYour final score: {self.score}/{len(self.questions)}")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Goodbye!")
                break
            else:
                self.score = 0  

quiz_game = QuizGame()
quiz_game.play_game()
