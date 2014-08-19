import sys


class BSTree(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def lowest_common_ancestor(self, value1, value2):
        if value1 <= self.value <= value2 or value1 >= self.value >= value2:
            return self.value
        if self.value > value1 and self.value > value2:
            if self.left:
                return self.left.lowest_common_ancestor(value1, value2)
        elif self.value < value1 and self.value < value2:
            if self.right:
                return self.right.lowest_common_ancestor(value1, value2)


if __name__ == '__main__':
    tree = BSTree(30)
    tree.left = BSTree(8)
    tree.right = BSTree(52)
    tree.left.left = BSTree(3)
    tree.left.right = BSTree(20)
    tree.left.right.left = BSTree(10)
    tree.left.right.right = BSTree(29)
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f.readlines():
            line = line.rstrip().split()
            if line:
                lca = tree.lowest_common_ancestor(int(line[0]), int(line[1]))
                if lca:
                    print str(lca)
