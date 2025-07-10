"""
Lesson 08 ICE - Dictionaries & Compound Values
CSE 111
Author: [Your Name]
Description:

Practice using a compound dictionary to track a store's inventory.

Instructions:

Complete the following program to help a small grocery store
track inventory items by SKU code.

For each SKU, you will store the item name, aisle, and quantity. 
Store the inventory in a dictionary where the key is the SKU number
and the value is a list containing the [item name, aisle, quantity].

Menu options let a clerk add new items, restock, look up a
single item, print the full inventory, and show the total
quantity of all items combined.
"""

# ----- index constants -----
NAME_INDEX  = 0
AISLE_INDEX = 1
QTY_INDEX   = 2

def main():
    # 1) Seed inventory with at least five items
    inventory = {
        # "SKU": [name, aisle, qty]
        "A100": ["Apples", 1, 50],
        "B200": ["Milk", 2, 75],
        "C355": ["Steak", 15, 20],
        "D430": ["Chicken", 15, 25],
        "L830": ["Eggs", 1, 20]
    }

    # Menu
    while True:
        print("\n1 Add  2 Restock  3 Lookup  4 Print all  5 Total qty  6 Quit")
        choice = input("Select: ").strip()
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            restock_item(inventory)
        elif choice == "3":
            lookup_item(inventory)
        elif choice == "4":
            print_inventory(inventory)
        elif choice == "5":
            print_total(inventory)
        elif choice == "6":
            break
        else:
            print("Invalid option")

# ---------- helper functions ----------
def add_item(inv):
    # TODO: ask for SKU, name, aisle, quantity and
    #       add to dictionary only if SKU not present
    sku = input("New SKU: ")
    name = input("Item name: ")
    aisle = int(input("Aisle number: "))
    quantity = int(input("Quantity: "))
    inv[sku] = [name, aisle, quantity]

def restock_item(inv):
    # TODO: ask for SKU and amount; increase quantity if found
    item = input("What item to restock?: ")
    new_total = int(input("How many: "))
    if item == NAME_INDEX:
        inv[QTY_INDEX] = inv[new_total]

def lookup_item(inv):
    # TODO: ask for SKU; display info about the item or “not found”
    item = input("Enter item SKU: ")
    if item not in inv:
        print("Item not found")

def print_inventory(inv):
    # TODO: iterate by using for sku, data in inv.items():
    #       print nicely formatted line showing each item in the inventory
    for key in inv:
        print(f"{key}: {inv[key]}")

def print_total(inv):
    # TODO: sum the QTY_INDEX of every inner list and print the sum
    total = 0
    for key in inv:
        total += inv[key][QTY_INDEX]
    print(total)

# ---------- run program ----------
if __name__ == "__main__":
    main()
