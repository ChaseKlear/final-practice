from testing_utils import run_a_test
from question_2 import generate_and_process_data
from random import seed

seed(1337)

def test_q2_generate_and_process_data_1():
    run_a_test(generate_and_process_data, [419904, -1], 1, 2, 3)


def test_q2_generate_and_process_data_2():
    run_a_test(generate_and_process_data, [46656, 23328], 2, 1, 3)


def test_q2_generate_and_process_data_3():
    run_a_test(generate_and_process_data, [32, 128, 128, 128, -1, -1], 4, 3, 2)


def test_q2_generate_and_process_data_4():
    run_a_test(generate_and_process_data, [512, 2048, 128, -1], 3, 4, 2)


def test_q2_generate_and_process_data_5():
    run_a_test(generate_and_process_data, [12597120000, 530841600, 135475200], 3, 3, 10)


def test_q2_generate_and_process_data_6():
    run_a_test(generate_and_process_data, [], 0, 0, 0)
