import pytest
from stack import Stack
from stack import Node


@pytest.fixture(scope='function')
def simple_stack():
    stack = Stack()
    node1 = Node(1, None)
    node2 = Node(2, node1)
    stack.head = node2
    return stack


@pytest.fixture(scope='function')
def codeeval_input1():
    stack = Stack()
    node1 = Node(1, None)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    node4 = Node(4, node3)
    stack.head = node4
    return stack


@pytest.fixture(scope='function')
def codeeval_input2():
    stack = Stack()
    node1 = Node(10, None)
    node2 = Node(-2, node1)
    node3 = Node(3, node2)
    node4 = Node(4, node3)
    stack.head = node4
    return stack


def test_make_new_stack():
    stack = Stack()
    assert stack.head is None


def test_push_to_empty_stack():
    stack = Stack()
    stack.push(1)
    assert stack.head.value == 1
    assert stack.head.next_node is None


def test_push_to_stack(simple_stack):
    stack = simple_stack
    stack.push(3)
    assert stack.head.value == 3
    assert stack.head.next_node.value == 2
    assert stack.head.next_node.next_node.value == 1
    assert stack.head.next_node.next_node.next_node is None


def test_pop_from_empty_stack():
    with pytest.raises(LookupError):
        stack = Stack()
        stack.pop()


def test_pop_from_stack(simple_stack):
    stack = simple_stack
    assert stack.pop() == 2
    assert stack.head.value == 1
    assert stack.head.next_node is None


def test_write_codeeval_output_1(codeeval_input1):
    stack = codeeval_input1
    assert stack.write_output() == '4 2'


def test_write_codeeval_output_2(codeeval_input2):
    stack = codeeval_input2
    assert stack.write_output() == '4 -2'
