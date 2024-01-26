# Repeat ex. ty25. But this time represent's the famous person's name using a variable famous_person
# Then compose your message and represent it with a new variable called message. Print your message.

famousPerson1 = "Albert Einstein"
famousPerson2 = "Eleanor Roosevelt"

message1 = "Life is like riding a bicycle. To keep your balance, you must keep moving."
message2 = "No one can make you feel inferior without your consent."

quoteDecision = input("Would you like to read a quote from Einstein (1) or Roosevelt (2)?: ")
if quoteDecision == "1":
    print(f'{famousPerson1} once said: "{message1}"')
else:
    print(f'{famousPerson2} once said: "{message2}"')