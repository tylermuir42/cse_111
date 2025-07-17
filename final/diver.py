"""This will be where I write the python
    for my Helldivers 2 Stratagem Planner
    
    A mission log is in mission_log.csv
    A list of stratagems is in stratagems.csv"""

import csv
import random
from datetime import datetime

DATE_INDEX = 0
DIFFICULTY_INDEX = 1
ENEMY_INDEX = 2
WIN_INDEX = 3

def main():
    print("Welcome to the unofficial Helldivers 2 Loadout Tracker!")
    display_menu()
    

def show_options():
    """I should have figured out how to make this
    work in the display menu function but I gave up.
    """
    print("1. Log a new mission")
    print("2. View mission log")
    print("3. Create random stratagem loadout")
    print("4. Calculate success rate")
    print("Press 'q' to quit")

def display_menu():
    """Displays the menu the to command line
    """
    show_options()
    while True:  
        print()
        choice = input("Choose an option: ")
        print()
        if choice == '1':
            log_mission()
            show_options()
        elif choice == '2':
            show_mission_log()
            show_options()
        elif choice == '3':
            random_stratagem_loadout()
            show_options()
        elif choice == '4':
            calculate_success_rate()
        elif choice.lower() == "q":
            exit()


def log_mission():
    """Stores other information to write 
        to missions.csv"""
    
    #Gets the current date and time
    #and uses it for the key value
    date = datetime.now().strftime("%m/%d/%Y %H:%M")

    #Check that the difficulty is an integer
    while True: 
        try:
            difficulty = int(input("Enter the difficulty (1-10): "))
            break
        except ValueError as val_err:
            # This code will be executed if the user enters
            # an invalid integer for the line number.
            print("Invalid input. Please enter a whole number")

    #Check that the enemy input is correct
    while True:
        enemy = input("Enter enemy type. 'a' for automatons, 't' for terminids, 'i' for illuminate: ").lower()

        #Change enemy input to match the csv file
        #and check to make sure it's correct
        if enemy.lower() == "a":
            enemy = "Bots"
            break
        elif enemy.lower() == "t":
            enemy = "Bugs"
            break
        elif enemy.lower() == 'i':
            enemy = "Squids"
            break
        else:
            print("You entered an invalid letter for the enemy type.")
            print("Run the program again and enter an 'a', 't', or 'i'")


    while True: 
        result = input("Did you win? (y/n): ")

        #Change result input to match the csv file
        if result.lower() == "y":
            result = "Win"
            break
        elif result.lower() == "n":
            result = "Lose"
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'")

    #Log all the inputs to the csv file
    with open("mission_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, difficulty, enemy, result])

    print("Mission logged successfully.")


def show_mission_log():
    """Displays the mission log from the csv file
    and prints to the terminal
    """
    mission_dict = read_log("mission_log.csv", DATE_INDEX)

    for mission_date, mission_data in mission_dict.items():
        try:
            if mission_date in mission_dict:
                date = mission_data[DATE_INDEX]
                difficulty = mission_data[DIFFICULTY_INDEX]
                enemy = mission_data[ENEMY_INDEX]
                win = mission_data[WIN_INDEX]
                print(f"{date}: {enemy}  Difficulty-{difficulty} Result-{win}")
            else:
                print(f"Mission on date {mission_date} not found.")
                print()

        except KeyError:
            print(f"Mission {mission_date} not found.")
    print()


def calculate_success_rate():
    """Calculates the success rate of all missions
    and prints to the terminal
    """
    log = read_log("mission_log.csv", DATE_INDEX)

    total = 0
    wins = 0

    for mission_date, mission_data in log.items():
        try:
            result = mission_data[WIN_INDEX].strip().lower()
            total += 1
            if result == 'win':
                wins += 1
        except KeyError:
            print(f"Mission {mission_date} not found.")

    if total > 0:
        ratio = wins / total
        print(f"Win/Lose ratio: {ratio:.2f}")
    else:
        print("No missions recorded")


def random_stratagem_loadout():
    """Crates a random stratagem loadout
    and prints to the terminal
    """
    stratagems_dict = read_log("stratagems.csv", 0)
    strats = random.sample(list(stratagems_dict.items()), 4)
    for strat in strats:
        print(f"{strat[0]}")
    print()


def read_log(filename, key_col):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    log = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_col]
                log[key] = row_list

    return log


if __name__ == "__main__":
    main()
