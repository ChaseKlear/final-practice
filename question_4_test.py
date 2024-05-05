from testing_utils import run_a_test
from question_4 import in_place_update_average

def test_q4_in_place_update_average_1():
    run_a_test(in_place_update_average, [2.5, 4], [1, 2, 3, 4])


def test_q4_in_place_update_average_2():
    run_a_test(in_place_update_average, [2.5, 4], [4, 3, 2, 1])


def test_q4_in_place_update_average_3():
    run_a_test(in_place_update_average, [3.1428571428571104, 7], [1337, 3, 2, 1, 9, 7, -1337])
