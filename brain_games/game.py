import prompt
def game(task, nik, what_is_the_correct_answer, check_condition, correct_answer):
    print(what_is_the_correct_answer)
    for i in range(3):
        question = task()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        condition = check_condition(question, answer)
        if condition:
            print("Correct!")
        else:
            print(f"'{answer}' is the wrong answer ;(. Correct answer was '{correct_answer(question)}' \nLet's try again, {nik}!")
            break
        if i == 2:
            print(f"Congratulations, {nik}!")
