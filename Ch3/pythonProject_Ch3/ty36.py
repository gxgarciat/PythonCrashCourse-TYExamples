# More guests: You just found a bigger dinner table, so more space is available. Think of 3 more guests
# guests to invite to dinner.
# 1. Start your program from exercise 3.4 - 3.5. Add a print() call, to inform you found a bigger table
# 2. Use insert() to add a new guest to the beginning of your list
# 3. Use insert() to add a new guest to the middle of your list
# 4. Use append() to add one new guest to the end of your list
# 5. Print a new set of invitations, one for each person in your list.

from random import randint

# Part 1
guessList = ["Gandhi", "Napoleon", "Simon Bolivar", "Messi"]

rd1 = randint(0, len(guessList) - 1)
print("------Dinner invitation-------")
print(f'Hi {guessList[0]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[1]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[2]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[3]}, when are you available? I would like to invite you to dinner.')
print("---------------------------------")
print(f"We found a bigger table! And we would like to invite three more people!")
print("---------------------------------")
# Part 2 to 4
newPerson1 = input("Who would you like to invite first? ")
newPerson2 = input("Who would you like to invite second? ")
newPerson3 = input("Who would you like to invite third? ")
guessList.insert(0,newPerson1)
guessList.insert(round(len(guessList)/2)+1,newPerson2)
guessList.append(newPerson3)
print(len(guessList))

# Part 5
print("")
print("------Dinner invitation-------")
print(f'Hi {guessList[0]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[1]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[2]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[3]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[4]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[5]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[6]}, when are you available? I would like to invite you to dinner.')

