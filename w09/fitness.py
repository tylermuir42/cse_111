# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():

    # Get the user's gender, birthdate, height, and weight.
    gender = input("Enter your gender: (M/F): ")
    birthdate = input("Enter your birthday in YYYY-MM-DD format: ")
    weightStone = input("Would you like to have your weight in stones? (Y/N): ")
    if weightStone.lower() == 'y':
        weightLbs = float(input("Enter your weight in stones: "))
        weightLbs = stone_from_lbs(weightLbs)
    else: 
        weightLbs = float(input("Enter your weight in pounds: "))
    heightInches = input("Enter your height in feet and inches in FF-II: ").split("-")
    totalInches = footInches(*heightInches) # * unpacks the heightInches

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.

    # Print the results for the user to see.
    age = compute_age(birthdate)
    kg = kg_from_lb(weightLbs)
    cm = cm_from_in(totalInches)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, age)

    print(f"Age: {age}")
    print(f"Weight in kg: {kg:.2f}kg")
    print(f"Height in m: {(cm / 100):.2f}m")
    print(f"BMI: {bmi:.1f}")
    print(f"BMR: {bmr:.1f}")


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    
    return(pounds * 0.45359237)


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return(inches * 2.54)

def stone_from_lbs(weight):
    return(weight * 14)

def footInches(foot, inches):
    return((float(foot) * 12) + float(inches))

def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return((10000 * weight) / (height**2))


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.lower() == 'm':
        return(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
    elif gender.lower() == 'f':
        return(447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age))


# Call the main function so that
# this program will start executing.
main()
