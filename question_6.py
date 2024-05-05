"""
Question 6 (Booleans/Loops)

Description:
Implement a function that given a string "operator" that can be "and", "or", or "xor", returns a
2D list that represents a truth table of all the possible combinations of 2 boolean values.

The inner list should have 3 values, the first boolean value, the second boolean value,
and the result of the expression of the two boolean values using the operator

If an invalid operator string is passed, return an empty list

Examples:
    truth_table('and') -> [[False, False, False], [False, True, False], [True, False, False], [True, True, True]]
    truth_table('or') -> [[False, False, False], [False, True, True], [True, False, True], [True, True, True]]
    truth_table('xor') -> [[False, False, False], [False, True, True], [True, False, True], [True, True, False]]
    truth_table('invalid') -> []

HINT: 0 = False and 1 = True when casting an integer to a boolean
"""
def truth_table(operator: str) -> list[list[bool, bool, bool]]:
    pass  # Your code goes here
