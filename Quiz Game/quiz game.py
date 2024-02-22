import random

class QuizGame:
    def __init__(self):
        self.q = [{"q": "Capital of Japan?", "o": ["Seoul", "Beijing", "Tokyo", "Bangkok"], "a": "Tokyo"},
                  {"q": "Element with symbol 'O'?", "o": ["Oxygen", "Osmium", "Ozone", "Ochre"], "a": "Oxygen"},
                  {"q": "'Red Planet'?", "o": ["Earth", "Mars", "Venus", "Jupiter"], "a": "Mars"},
                  {"q": "Capital of Australia?", "o": ["Sydney", "Melbourne", "Canberra", "Brisbane"], "a": "Canberra"},
                  {"q": "Currency of Brazil?", "o": ["Dollar", "Euro", "Real", "Yen"], "a": "Real"},
                  {"q": "Author of '1984'?", "o": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Arthur C. Clarke"], "a": "George Orwell"},
                  {"q": "Largest ocean?", "o": ["Atlantic", "Indian", "Arctic", "Pacific"], "a": "Pacific"}]
        self.s = 0
    def w(self):
        print("Welcome to the Quiz Game!\nAnswer the following questions and test your knowledge.")

    def qd(self, d):
        print(f"\nQuestion: {d['q']}")
        for i, o in enumerate(d["o"], 1):
            print(f"{i}. {o}")

    def ua(self):
        while True:
            u = input("choose (1, 2, 3, or 4): ")
            if u.isdigit() and 1 <= int(u) <= 4:
                return int(u)
            print("Invalid input. choose between 1 and 4.")

    def ea(self, u, a):
        r = "Correct! Well done!" if u == a else f"Incorrect. Correct answer: {a}"
        print(r)
        self.s += 1 if u == a else 0

    def pg(self):
        self.w()
        while True:
            random.shuffle(self.q)
            for d in self.q:
                self.qd(d)
                u = self.ua()
                a = d["o"].index(d["a"]) + 1
                self.ea(u, a)
            print(f"\nYour final score: {self.s}/{len(self.q)}")
            p = input("Play again? (yes/no): ").lower()
            if p != "yes":
                print("Goodbye!")
                break
            self.s = 0

QuizGame().pg()
