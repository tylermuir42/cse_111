# Create a dictionary to keep track of inventory at a grocery store
inventory = {
    # item: [price, qty]
    "bread": [2.99, 34],
    "milk": [4.50, 14],
    "eggs": [7.00, 89],
    "meat": [12.99, 5]
}

PRICE_INDEX = 0
QUANTITY_INDEX = 1
print(f"Bread: ${inventory["bread"][PRICE_INDEX]:.2f} "
      f"{inventory["bread"][QUANTITY_INDEX]}")



# Remove bread
print(inventory)
inventory.pop("bread")
print(inventory)

# Update the milk qty
inventory["milk"][QUANTITY_INDEX] = 50
print(inventory)

# Add meat
if "meat" not in inventory:
    # add it
    inventory["meat"] = [8.99, 45]
print(inventory)


# # Fix an item
# inventory["eggs"].pop()
# print(inventory)




# Number of products in the store
print(len(inventory))


# Add up all the items qty
total = 0
for key, value in inventory.items():
    total += value[QUANTITY_INDEX]

print(total)

total = 0
for key in inventory:
    total += inventory[key][QUANTITY_INDEX]

print(total)








# How much does bread cost?


# How much does cheese cost?


# Add eggs



# Remove bread



# How many items are in our store?



# Check if we have milk in the store



