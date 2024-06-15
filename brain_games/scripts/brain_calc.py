import prompt
import random
from brain_games.game  import game
from brain_games.cli import welcome_user

def main():
    def check_condition(otvet, answer):
        nums = otvet.split()
        a = int(nums[0])
        b = int(nums[2])
        if nums[1] == '+':
            res = a + b
        if nums[1] == '-':
            res = a - b
        if nums[1] == '*':
            res = a * b
        string = str(res)

        return answer == string

    def correct_answer(otvet):
        nums = otvet.split()
        a = int(nums[0])
        b = int(nums[2])
        if nums[1] == '+':
            res = a + b
        if nums[1] == '-':
            res = a - b
        if nums[1] == '*':
            res = a * b
        return res
    
    i = 1 

    def question():

        nonlocal i
        a = random.randint(1,1000)
        b = random.randint(1,1000)
        if i == 1:
            i+=1
            return f'{a} + {b}'
             
        if i == 2: 
            i+=1
            return f'{a} - {b}'

        if i == 3:
            i+=1
            return f'{a} * {b}'
        

    s = 'What is the result of the expression?'
    name = welcome_user()
    game(question, name, s, check_condition, correct_answer)


if __name__ == '__main__':
    main()
