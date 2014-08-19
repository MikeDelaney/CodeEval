import pytest
from lca import BSTree


@pytest.fixture(scope='function')
def example_tree():
    tree = BSTree(30)
    tree.left = BSTree(8)
    tree.right = BSTree(52)
    tree.left.left = BSTree(3)
    tree.left.right = BSTree(20)
    tree.left.right.left = BSTree(10)
    tree.left.right.right = BSTree(29)
    return tree


def test_init():
    tree = BSTree(1)
    assert tree.value is 1
    assert tree.left is None
    assert tree.right is None


def test_lowest_common_ancestor_1(example_tree):
    tree = example_tree
    assert tree.lowest_common_ancestor(8, 52) == 30


def test_lowest_common_ancestor_2(example_tree):
    tree = example_tree
    assert tree.lowest_common_ancestor(3, 29) == 8


def test_lowest_common_ancestor_3(example_tree):
    tree = example_tree
    assert tree.lowest_common_ancestor(10, 29) == 20


def test_lowest_common_ancestor_4(example_tree):
    tree = example_tree
    assert tree.lowest_common_ancestor(20, 52) == 30


def test_lowest_common_ancestor_5(example_tree):
    tree = example_tree
    assert tree.lowest_common_ancestor(8, 20) == 8
