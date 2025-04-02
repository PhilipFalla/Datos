class Node:
    def __init__(self, data: str):
        self.data = data
        self.right_child = None
        self.left_child = None

    def __repr__(self):
        return '( {} ) <- |({})| -> ( {} )'.format(self.left_child, self.data, self.right_child)

class BinaryTree:
    def __init__(self):
        self.root = None

    