from typing import Any
from node import Node

"""
Question 3 (Nodes):

Description:
Given a list of values, create a list of nodes so that each nodes value in the resulting list is the same
as what was passed in the values list
[ e.g. values[i] == result[i].get_value() ]
The next value of the nodes should be the next node in the list
[ e.g. result[i].get_next() == result[i + 1] ]
that last nodes next node should be None
[ e.g. result[-1].get_next() == None ]

Example:
    node = (value, next_value)
    linked_list([1, 2, 3]) -> [(1, 2), (2, 3), (3, None)]
"""
def linked_list(values: list[Any]) -> list[Node]:
    pass  # Your code goes here