from typing import Tuple


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

    def go_right(self) -> Tuple['ListNode', bool]:
        if self.right:
            new_node, is_last = self.right.go_right()
            if is_last:
                self.right = new_node.left
            return new_node, False
        else:
            return self, True

    def go_left(self) -> Tuple['ListNode', bool]:
        if self.left:
            new_node, is_last = self.left.go_left()
            if is_last:
                self.left = new_node.right
            return new_node, False
        else:
            return self, True

    def remove_this_node(self):
        if self.left:
            new_node, is_last = self.left.go_right()
            if is_last:
                self.left = new_node.left
            self.value = new_node.value
        elif self.right:
            new_node, is_last = self.right.go_left()
            if is_last:
                self.right = new_node.right
            self.value = new_node.value
        else:
            self.value = None


root = ListNode(5)
root.add_child(3)
root.add_child(7)
root.add_child(4)
root.add_child(2)
root.add_child(1)
root.add_child(2.5)
root.add_child(3)
root.add_child(4.5)
root.add_child(4.3)
root.add_child(5.5)
root.add_child(6)
root.add_child(8)
root.add_child(10)
root.add_child(7.5)

print(root.is_exists(5))


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left, level + 1)


if __name__ == '__main__':
    print_tree(root)
    print()
    root.remove_this_node()
    print()
    print_tree(root)
