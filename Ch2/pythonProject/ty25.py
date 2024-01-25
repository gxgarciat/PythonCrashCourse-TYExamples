# Famous quote: Find a quote from a famous person you admire. Print the quote and the
# name of its author. Your output should include the quotation marks.

einsteinQuote = "Life is like riding a bicycle. To keep your balance, you must keep moving."
rooseveltQuote = "No one can make you feel inferior without your consent."

quoteDecision = input("Would you like to read a quote from Einstein (1) or Roosevelt (2)?: ")
if quoteDecision == "1":
    print(f'Albert Einstein once said: "{einsteinQuote}"')
else:
    print(f'Eleanor Roosevelt once said: "{rooseveltQuote}"')