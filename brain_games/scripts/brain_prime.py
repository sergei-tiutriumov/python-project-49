import prompt
import random
from brain_games.game  import game
from brain_games.cli import welcome_user

def main():
    def check_condition(question, answer):
        nonlocal i
        d = 2
        while i % d != 0:
            d += 1
        if (answer == 'yes' and d == i) or (answer == 'no' and d != i):
            return True
        else:
            return False

    def correct_answer(question):
        d = 2
        nonlocal i
        while i % d != 0:
            d += 1
        if d == i:
            return 'yes'
        else:
            return 'no'
    i = 0

    def question():
        nonlocal i
        chislo = random.randint(2,100)
        i = chislo
        return chislo

    s = 'Answer "yes" if given number is prime. Otherwise answer "no"'
    name = welcome_user()
    game(question, name, s, check_condition, correct_answer)


if __name__ == '__main__':
    main()
