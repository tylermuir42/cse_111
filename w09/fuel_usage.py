def main():
    # Get an odometer value in U.S. miles from the user.
    odometer1 = int(input("Enter the first odometer number: "))

    # Get another odometer value in U.S. miles from the user.
    odometer2 = int(input("Enter the second odometer number: "))

    # Get a fuel amount in U.S. gallons from the user.
    gallons = (float(input("How many gallons of fuel?: ")))

    # Call the miles_per_gallon function and store
    mpg = miles_per_gallon(odometer1, odometer2, gallons)
    # the result in a variable named mpg.

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lpk = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f"Miles per gallon: {mpg:.2f}")
    print(f"LPK100K: {lpk:.2f}")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    total_miles = end_miles - start_miles
    mpg = total_miles / amount_gallons

    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lpk = 235.215 / mpg
    return lpk


# Call the main function so that
# this program will start executing.
main()