import csv

"""
Question 5 (Data Manipulation/CSVs/Algorithms)

For a credit card, the number on the front isn't completely random.
The first digit represents the general industry of the card's usage (e.g. 1/2 for airlines)
the next five digits represent the card's network (e.g. visa/mastercard)
every digit after that, except for the last digit, is the account number issued to the card owner
the last digit is called the check digit. This digit is calculated using the special algorithm that works as follows
    1) remove the last digit from the card number as this is the check digit and shouldn't be involved in the calculation
    2) starting from the last digit of the remaining number, double every other digit
    3) if the doubled number is more than 10, add the two digits together (i.e. 8 * 2 = 16 -> 1 + 6 = 7)
    4) add all the digits together, including the ones you didn't double
    5) subtract the last digit of the sum you calculated in step 4 from 10 (if the last digit of the sum is 0, your check digit is 0)
    What you get should be the check digit of a valid credit card

Implement fraud_cards so that it reads through a CSV containing credit card data (in this case `credit_cards.csv` in the data folder) and
returns a list of names who have fraudulent credit cards.

if the filename doesnt exist, return None
you can assume there is no invalid information (e.g. a letter in a credit card number)
"""
def fraud_cards(filename: str) -> list[str] | None:
    pass  # Your code goes here