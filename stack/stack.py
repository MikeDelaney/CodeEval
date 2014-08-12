
class Node(object):
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.head:
            retval = self.head.value
            self.head = self.head.next_node
            return retval
        raise LookupError

    def write_output(self):
        output = ''
        count = 1
        while self.head:
            if count % 2 != 0:
                output += str(self.pop()) + ' '
            else:
                self.pop()
            count += 1
        return output.rstrip()
