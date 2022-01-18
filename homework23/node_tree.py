class ListNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value}'

    def add_child(self, value):
        if value < self.value:
            if self.left is None:
                self.left = ListNode(value)
            else:
                self.left.add_child(value)
        else:
            if self.right is None:
                self.right = ListNode(value)
            else:
                self.right.add_child(value)

    def is_exists(self, value) -> bool:
        if value == self.value:
            return True
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.is_exists(value)
        if value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.is_exists(value)

    def remove_this_node(self, root, value):
        pass


# queue - FIFO
# stack - LIFO

root = ListNode(5)
root.add_child(3)
root.add_child(7)
root.add_child(4)
root.add_child(2)
root.add_child(1)
root.add_child(2.5)
root.add_child(3)
root.add_child(4.5)
root.add_child(5.5)
root.add_child(6)
root.add_child(8)
root.add_child(10)
root.add_child(7.5)

print(root.is_exists(5))
print(root.remove_this_node(root, 10))


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left, level + 1)


if __name__ == '__main__':
    print_tree(root)
