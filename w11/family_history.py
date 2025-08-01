# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1695, 1752],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1737, 1803],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1802, 1858],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1899, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1829],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)

    count_marriages(marriages_dict, people_dict)


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    for key in people_dict:
        death_age = people_dict[key][DEATH_YEAR_INDEX] - people_dict[key][BIRTH_YEAR_INDEX]
        print(f"{people_dict[key][NAME_INDEX]}  Age: {death_age}")
        print(f"Born: {people_dict[key][BIRTH_YEAR_INDEX]} Died: {people_dict[key][DEATH_YEAR_INDEX]}")
        print()


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    male_count = 0
    female_count = 0
    for key in people_dict:
        gender = people_dict[key][GENDER_INDEX]
        if gender == "M":
            male_count += 1
        else:
            female_count += 1
    print(f"Male: {male_count}")
    print(f"Female: {female_count}")


def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    for key in marriages_dict:
        husband_key = marriages_dict[key][HUSBAND_KEY_INDEX]
        wife_key = marriages_dict[key][WIFE_KEY_INDEX]
        husband_name = people_dict[husband_key][NAME_INDEX]
        husband_age = marriages_dict[key][WEDDING_YEAR_INDEX] - people_dict[husband_key][BIRTH_YEAR_INDEX]
        wife_name = people_dict[wife_key][NAME_INDEX]
        wife_age = marriages_dict[key][WEDDING_YEAR_INDEX] - people_dict[wife_key][BIRTH_YEAR_INDEX]
        marriage_year = marriages_dict[key][WEDDING_YEAR_INDEX]
        print(f"{husband_name} was {husband_age} years old when he married"
              f" {wife_name} who was {wife_age} years old in {marriage_year}.")
        

def count_marriages(marriages_dict, people_dict):
    """Count and print the number of times that each person married.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print("Number of Marriages")

    NUM_MARRIAGES_INDEX = 4

    # Add an extra variable to each person_list. The variable will
    # be used to count the number of marriages that each person had.
    for person_key, person_list in people_dict.items():
        person_list.append(0)

    # For each marriage in the marriage dictionary,
    # add one to the husband's number of marriages
    # and add one to the wife's number of marriages.
    for marriage_key, marriage_list in marriages_dict.items():

        # Get the husband person key and the wife person key.
        husband_key = marriage_list[HUSBAND_KEY_INDEX]
        wife_key = marriage_list[WIFE_KEY_INDEX]

        # Add one to the number of times
        # the husband has been married.
        husband_list = people_dict[husband_key]
        husband_list[NUM_MARRIAGES_INDEX] += 1

        # Add one to the number of times
        # the wife has been married.
        wife_list = people_dict[wife_key]
        wife_list[NUM_MARRIAGES_INDEX] += 1

    # For each person in the people dictionary, print the
    # person's name and number of times that person married.
    for person_key, person_list in people_dict.items():
        name = person_list[NAME_INDEX]
        num_marriages = person_list[NUM_MARRIAGES_INDEX]
        print(name, num_marriages) 



# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
