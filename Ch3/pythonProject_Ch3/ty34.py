# If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you'd like to invite to dinner
# Then use your list to print a message to each person, inviting them to dinner.

from random import randint

guessList = ["Gandhi", "Napoleon", "Simon Bolivar", "Messi"]

rd1 = randint(0, len(guessList) - 1)

print(f'Hi {guessList[rd1]}, when are you available? I would like to invite you to dinner.')