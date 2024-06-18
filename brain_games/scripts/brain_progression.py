import prompt
import random
from brain_games.game  import game
from brain_games.cli import welcome_user

def main():
    def check_condition(otvet, answer):
        nonlocal secret
        answer = int(answer)
        return answer == secret
  
    def correct_answer(otvet):
        nonlocal secret
        return secret
        
    secret = 0

    def question():
        nonlocal secret
        chisla = []
        i = 0
        for i in range(10):
            x = i*3
            chisla.append(x)
        mask = '..'
        index = random.randint(0, 9)
        secret = chisla[index]
        chisla[index] = mask
        stroka = ''
        for i in chisla:
            i = str(i)
            i += ' '
            stroka += i
        return f'{stroka}  '

        

    s = 'What number is missing in the progression?'
    name = welcome_user()
    game(question, name, s, check_condition, correct_answer)


if __name__ == '__main__':
    main()
