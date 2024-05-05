import random
from node_queue import Queue

"""
Question 2 (Queue):

Description:
The producer/consumer programming pattern works by having `producers` that constantly generate
some data from somewhere and as that data is generated, `consumers` will take that data and process
it. Normally, these run at the same time and work off of a shared Queue. Producers adding
data to be processed to the Queue and Consumers taking it off the Queue and processing it.
With multiple producers and consumers running at the same time (each producer/consumer only
responsible for 1 piece of data at a time), this can be a fast and efficient way to process data.

Even though we do not know how to make them run at the same time, we can still implement this pattern.

Implement a producer function that takes a Queue and a maximum n integer.
this function uses the max_n integer to generate (`produce`) a list of 15 random numbers
whose values range from 1 to max_n, then adds that list to a queue

Then implement a consumer function that takes a value from the queue and processes the product of
elements in the list, returning it. If the queue is empty before trying to process any data, return -1

Then implement generate_and_process_data so that it creates a shared Queue for the producers and
consumers to use, will create and run producers_n number of producers (with max_n passed in) and then
run consumer_n number of consumers to process that data. If consumer_n number of consumers isn't enough
to process all the data, create consumer_n more consumers until all the data is processed.
generate_and_process_data should return a list of values returned from the consumers.

Your results from generate_and_process_data will be what is tested.

Examples:
↓  ↑  generate_and_process_data(1, 1, 10) -> [1039]
↓  ↑  producers([], 10) -> None (shared_queue = [9, 4, 6, 2, 3, ..., 2])
-  -  consumers([[9, 4, 6, 2, 3, ..., 2]]) -> 1039

↓  ↑  generate_and_process_data(1, 2, 10) -> [1039, -1]
↓  ↑  producers([], 10) -> None (shared_queue = [9, 4, 6, 2, 3, ..., 2])
↓  ↑  consumers([[9, 4, 6, 2, 3, ..., 2]]) -> 1039
-  -  consumers([]) -> -1
"""
def producer(shared_queue: Queue, max_n: int) -> None:
    pass  # Your code goes here


def consumer(shared_queue: Queue) -> int:
    pass  # Your code goes here


def generate_and_process_data(producers_n: int, consumers_n: int, max_n) -> list:
    pass  # Your code goes here
