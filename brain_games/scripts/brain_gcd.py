import prompt
import random
from brain_games.game  import game
from brain_games.cli import welcome_user 
import math

def main():
    def check_condition(otvet, answer):
        nums = otvet.split()
        a = int(nums[0])
        b = int(nums[2])
        res = math.gcd(a, b)
        string = str(res)

        return answer == string
    def correct_answer(otvet):
        nums = otvet.split()
        a = int(nums[0])
        b = int(nums[2])
        res = math.gcd(a, b)
        return res    

    def question(): 
        a = random.randint(0,11)*2
        b = random.randint(0,11)*2
        return f'{a} & {b}'

    s = 'You  should find the greatest common divisor '
    name = welcome_user()
    game(question, name, s, check_condition, correct_answer)


if __name__ == '__main__':
    main()
