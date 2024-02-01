# Start with the list you used in Exercise 3.1, but instead of just printing each person's name,
# print a message to them. The text of each message should be the same, but each message should be
# personalized with the person's name.

friendNames = ["Andres", "Juan", "Daniel", "Alberto"]
decisionVar = int(input("Choose one of your friends: 0 - 3: "))
print(f'Good morning {friendNames[decisionVar]}, I hope you have a lovely evening my friend.')