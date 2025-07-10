def question():
    answer1 = check_answer(int(input("My ideal vacation spot would be a remote, wilderness area. ")))
    answer2 = check_answer(int(input("I always think about how my actions affect the environment. ")))
    answer3 = check_answer(int(input("My connection to nature and the environment is a part of my spirituality. ")))
    answer4 = check_answer(int(input("I take notice of wildlife wherever I am. ")))
    answer5 = check_answer(int(input("My relationship to nature is an important part of who I am. ")))
    answer6 = check_answer(int(input("I feel very connected to all living things and the earth. ")))

    total = answer1 + answer2 + answer3 + answer4 + answer5 + answer6
    score = total / 6
    return score

def check_answer(answer):
    if answer < 1:
        answer = 1
    elif answer > 5:
        answer = 5
    return answer

def main():
    score = question()
    print()
    print(f"Your score is {score}")

main()






