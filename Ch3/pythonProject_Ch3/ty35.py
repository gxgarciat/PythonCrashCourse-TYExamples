# You just heard that one of your guest can't make the dinner, so you need to send out a new set of
# invitations. You will have to think of someone else to invite.
# 1. Start with your program from exercise 3-4. Add print() call at the end of your program,
#    stating the name of the guest who can't make it.
# 2. Modify your list, replacing the name of the guest with the name of the new person you're inviting
# 3. Print a second set of invitation messages.

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
print(f"We heard that {guessList[rd1]} won't be able to dinner. We will miss you {guessList[rd1]}!")
print("---------------------------------")
newPerson = input("Who would you like to invite? ")
guessList[rd1] = newPerson
print("")
print("------Dinner invitation-------")
print(f'Hi {guessList[0]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[1]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[2]}, when are you available? I would like to invite you to dinner.')
print(f'Hi {guessList[3]}, when are you available? I would like to invite you to dinner.')