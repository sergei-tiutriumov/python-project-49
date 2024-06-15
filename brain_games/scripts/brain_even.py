import prompt
import random
from brain_games.game  import game
from brain_games.cli import welcome_user

def check_condition(question, answer):
    return (question % 2 == 0 and answer == 'yes') or (question % 2 != 0 and answer == 'no')
def correct_answer(question):
    return ('yes' if question % 2 == 0 else 'no')
def question():
     return (random.randint(1, 1000))

def main():
    s = 'Answer yes if the number is even, otherwise answer no'
    name = welcome_user()
    game(question, name, s, check_condition, correct_answer)


if __name__ == '__main__':
    main()
