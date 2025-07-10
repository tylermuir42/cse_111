#Nested dictionary

inventory = {
    "bread": {"price": 2.99, "qty": 25},
    "cheese": {"price": 3.99, "qty": 23},
}

print(inventory["bread"]["price"], inventory["bread"]["qty"])
print(inventory["cheese"]["price"], inventory["cheese"]["qty"])