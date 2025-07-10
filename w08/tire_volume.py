import math
from datetime import datetime

again = True

with open("volume.txt", mode="a") as volume_file:
    while again == True:
        width = float(input("Enter the width of the tire in mm: "))
        aspect = float(input("Enter the aspect ratio of the tire: "))
        diameter = float(input("Enter the diameter of the wheel in inches: "))
        purchase = input("Are you purchasing these tires? (Y/N): ")
        phone = "N/A"
        if purchase.lower() == "y":
            phone = input("Enter your phone number: ")

        volume = ((math.pi * (width ** 2) * aspect) * ((width * aspect) + (2540 * diameter)))
        volume /= 10_000_000_000

        now = datetime.now()

        print(f"{now.strftime('%m/%d/%Y %H:%M %p')} -- Volume: {volume:.2f} liters, Width: {width:.1f}mm, Aspect: {aspect:.1f}, Diameter: {diameter:.1f}in, Purchase: {purchase.upper()}, Phone: {phone}", file=volume_file)

        repeat = input("Would you like to make another input? (Y/N): ")
        repeat = repeat.lower()
        if repeat == "n":
            again = False