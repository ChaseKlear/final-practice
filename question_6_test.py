from testing_utils import run_a_test
from question_6 import truth_table

def test_q6_truth_table_1():
    run_a_test(truth_table, [[False, False, False], [False, True, False], [True, False, False], [True, True, True]], 'and')


def test_q6_truth_table_2():
    run_a_test(truth_table, [[False, False, False], [False, True, True], [True, False, True], [True, True, True]], 'or')


def test_q6_truth_table_3():
    run_a_test(truth_table, [[False, False, False], [False, True, True], [True, False, True], [True, True, False]], 'xor')


def test_q6_truth_table_4():
    run_a_test(truth_table, [], 'invalid')
