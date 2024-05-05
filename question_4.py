"""
Question 4 (Algorithms/Lists)

Description:
Write a function that, given a list of integers, returns a list of 2 values
The 0th index being the final average and the 1st index being the number of
values used to calculate the average.

Your function should implement the algorithm:
new_average = avg + ( value - avg ) / (n + 1)
    avg - the current average
    value - the value to be added to the dataset which the average was calculated with
    n - number of values used to calculate avg
to update the average IN-PLACE. this means you should not be creating a new list every
time, but working with the same result list throughout the functions runtime.

Your function should return a list of 2 values, the 0th index being the final average
and the 1st index being the number of values used to calculate the average.

Examples:
    in_place_update_average([1, 2, 3, 4]) -> [2.5, 4]

NOTE: while you may be able to make the test pass, the point of this question is to implement the algorithm
      and update the average as it gets values in the list rather than after finding a total sum.
"""
def in_place_update_average(data: list) -> list[int, int]:
    pass  # Your code goes here
