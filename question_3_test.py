from testing_utils import run_a_test
from question_3 import linked_list
from node import Node

def test_q3_linked_list_1():
    node3 = Node(3)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    run_a_test(linked_list, [node1, node2, node3], [1, 2, 3])


def test_q3_linked_list_2():
    run_a_test(linked_list, [], [])


def test_q3_linked_list_3():
    node3 = Node('c')
    node2 = Node('b', node3)
    node1 = Node('a', node2)
    run_a_test(linked_list, [node1, node2, node3], ['a', 'b', 'c'])


def test_q3_linked_list_4():
    node3 = Node(None)
    node2 = Node(None, node3)
    node1 = Node(None, node2)
    run_a_test(linked_list, [node1, node2, node3], [None, None, None])


def test_q3_linked_list_5():
    node3 = Node(3)
    node2 = Node(None, node3)
    node1 = Node('a', node2)
    run_a_test(linked_list, [node1, node2, node3], ['a', None, 3])
