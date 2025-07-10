# demo lists and some list methods

friends = ["Abraham", "Benjamin", "Caleb", "Daniel", "Elijah"]

# print a list of all friends
for friend in friends:
    print(friend)









# Add a new friend to the end of the list

friends.append("Felix") # Puts "Felix" at end of list
print(friends)

# Insert a friend in the middle of the list
friends.insert(1, "Boaz") # Put "Boaz" in the list at position 1
print(friends)

# Remove the last friend in the list
friends.pop() # removes "Felix"
print(friends)

# Remove a friend from anywhere in the list
friends.remove("Benjamin") # removes "Benjamin" from middle of list
print(friends)




