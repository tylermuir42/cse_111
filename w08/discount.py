from datetime import datetime
dt = datetime.now()

subtotal = 0
sales_tax = 0.06

price = 0

price = float(input("Enter the cost of your item: "))
while price != 0:
    quantity = int(input("How many of that item?: "))
    subtotal += (price * quantity)
    print(f"${subtotal:.2f}")
    price = float(input("Enter the cost of your item: "))

#Check for Tuesday or Wednesday
if dt.weekday() in (1,2) and subtotal >= 50:
    discount = subtotal * .1
    total = subtotal - discount
elif dt.weekday() in (1,2) and subtotal < 50:
    required = 50 - subtotal
    print(f"If you spend ${required:.2f} more dollars, you can get a discount!")

#Print total and discount
total += sales_tax * total
print(f"Discount: ${discount:.2f}")

print(f"Total: ${total:.2f}")