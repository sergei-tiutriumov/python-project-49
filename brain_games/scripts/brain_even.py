import prompt
import random


def main():
    a = "Welcome to the Brain Games!"
    print(a)
    name = prompt.string('May I have yout name?  ')
    print(f"Hello, {name} !")
    yes = 'yes'
    no = 'no'
    print(f'Answer {yes} if the mumber is even, otherwise answer {no} ')
    for i in range(3):
        question = random.randint(1, 1000)
        print(f'Question: {question} ')
        answer = prompt.string('Your answer: ')
        if((question%2 == 0 and answer == 'yes') or (question%2 != 0 and answer == "no")):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong  answer ;(. Correct answer was 'no' \nLet's try again, {name}!" if answer == yes else f"'{answer}' is wrong  answer ;(. Correct answer was 'yes' \nLet's try again, {name}!")
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
