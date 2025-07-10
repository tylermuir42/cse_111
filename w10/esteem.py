def convert_score(score):
    if score == "d":
        score = 0
    elif score == "D":
        score = 1
    elif score == "a":
        score = 2
    elif score == "A":
        score = 3
    return score

def negative_convert_score(score):
    if score == "A":
        score = 0
    elif score == "a":
        score = 1
    elif score == "d":
        score = 2
    elif score == "D":
        score = 3
    return score

def question():
    answer1 = input("I fell that I am a person of wroth, at least on an equal plane with others: ")

    answer2 = input("I fell that I have a number of good qualities: ")

    answer3 = input("All in all, I am inclined to feel that I am a failure: ")

    answer4 = input("I am able to do things as well as most other people: ")

    answer5 = input("I feel I do not have much to be proud of: ")

    answer6 = input("I take a positive attitude toward myself: ")

    answer7 = input("On the whole, I am satisfied with myself: ")

    answer8 = input("I wish I could have more respect for myself: ")

    answer9 = input("I certainly feel useless at times: ")

    answer10 = input("At times I think I am no good at all: ")

    return list(map(convert_score, [answer1, answer2, answer4, answer6, answer7])) + list(map(negative_convert_score, [answer3, answer5, answer8, answer9, answer10]))

def main():
    print("Enter D, d, a, or A to answer the following questions:")
    score = question()
    print()
    print (f"Your score is {sum(score)}")
    print("A score below 15 may indicate problematic low self-esteem.")

main()


