friends = ["Rohit", "Samuel", "James", "Kevin", "Andrew", "Olivia", "Amanda", "Jack", "Ethan", "Jack"]
lucky_numbers = [3, 4, 5, 33, 22, 25, 86, 42, 57, 486, 45, 245, 90, 88, 42, 21]
friends[1] = "Jaqueline"
# By doing friends.extend() I can pass any information onto the friends list
friends.extend(lucky_numbers)
# This will allow me to add indivual things to the list
friends.append()
# Insert places things into the list
friends.insert(1, "kelly")
# remove takes things out the list
friends.remove("Andrew")
# pop just removes last elements in the list
friends.pop()

# To search for particular things in the list (Kevin)
print(friends.index("Kevin"))
# Will tell you how many of an item is in the list
print(friends.count("Jack"))
# to print out the code in the list alphabetically 
lucky_numbers.sort()
print(lucky_numbers)

# To copy a list
friends2 = friends.copy()

print(friends[1:])