"""
Lesson 06 ICE - Debugging functions
CSE 111
Author: [Your Name Here]
Description:

Practice debugging functions by fixing the code below.

You may add additional print statements and/or use the 
debugger to help you.


Instructions:
    1. Fix the below code so it correctly calculates the monthly payment
       on a loan.

    2. (Stretch) Add a second function called "compute_total_payment" that multiplies
       the monthly payment by the total number of months to show how much
       the user will pay in total over the life of the loan.

    3. (Stretch) Write a test function in a separate file to test your computer_monthly_payment
       and compute_total_payment functions using pytest.

Notes:
Use the website https://www.calculator.net/amortization-calculator.html to 
check your calculations.

To calculate the monthly payment on a loan, the formula is:

          P * r
M =   -------------
                 -n
        1 - (1+r)

where

M  Monthly payment you will owe
P  Principal - the amount borrowed
r  Periodic interest rate, the annual rate divided by 12
n  Total number of payments, which is the number of years times 12

"""

def main():
    principal = float(input("Enter the loan amount: "))
    rate = float(input("Enter the annual rate (as a decimal, e.g., 0.06): "))
    years = int(input("How many years is the loan for? "))
    monthly_payment = compute_monthly_payment(principal, rate, years)
    total_payment = compute_total_payment(monthly_payment, years)

    print(f"Monthly payment is: ${monthly_payment:.2f}")
    print(f"Total payment is: ${total_payment:.2f}")

def compute_monthly_payment(p, r, y):
    months = y * 12
    monthly_rate = r / 12
    return (p * monthly_rate) / (1 - (1 + monthly_rate) ** -months)

def compute_total_payment(m, y):
    return m * y


if __name__ == "__main__":
    main()
