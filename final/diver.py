"""This will be where I write the python
    for my Helldivers 2 Stratagem Planner
    
    A mission log is in missions.csv
    A list of stratagems is in stratagems.csv"""

import csv
import random

def main():
    ...

def log_loadout(strat1, strat2, strat3, strat4, primary, secondary, armor):
    """Stores the loadout used for each run
        to be later stored in missions.csv

    Args:
        strat1 (string): Stratagem 1
        strat2 (string): Stratagem 2
        strat3 (string): Stratagem 3
        strat4 (string): Stratagem 4
        primary (string): Primary Weapon
        secondary (string): Secondary Weapon
        armor (string): Armor
    """
    ...
         

def log_mission(date, difficulty, enemy, loadout, win):
    """Stores other information to write 
        to missions.csv

    Args:
        date (string): Date of the mission
        difficulty (int): Mission difficulty 1-10
        enemy (string): Enemy type fought
        loadout (string): Gets the loadout from log_loadout()
        win (string): Win or loss
    """
    ...

def calculate_success_rate(win):
    """Calculates the success rate of all missions

    Args:
        win (_type_): _description_
    """

def random_stratagem_loadout():
    """Generates a random stratagem loadout
        for use in challenge runs
    """

def display_menu():
    """Displays the menu the the command line
    """


if __name__ == "__main__":
    main()
