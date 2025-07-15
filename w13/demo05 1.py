# use sorted for a compound list

# List of people with names and ages
people = [
    {"name": "Alice", "age": 30},
    {"name": "Zed", "age": 25},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Dave", "age": 25}
]

sorted_people = sorted(people, key=lambda person: person['age'])
# sorted_people = sorted(people, key=lambda person: f"{person['age']} + {person['name']}")

print(sorted_people)