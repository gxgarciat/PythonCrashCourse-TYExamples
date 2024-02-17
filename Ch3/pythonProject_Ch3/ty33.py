# Your own list: Think of your favourite mode of transportation, such as a motorcycle or a car,
# and make a list that stores several examples. Use your list to print a series of statements
# these items, such as "I would like to own a Honda motorcycle.
from random import randint

transportationMode = ["motorcycle", "car", "bike"]
randomBrands = ["Ford", "Yamaha", "Cervelo", "Harley"]

rd1 = random.randint(0,len(transportationMode)-1)
rd2 = random.randint(0,len(randomBrands)-1)

print(f'I would like to buy a {randomBrands[rd2]} {transportationMode[rd1]}')