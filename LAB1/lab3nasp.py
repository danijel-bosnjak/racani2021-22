class Node:
    def __init__(self, scala = 3):
        self.values = []
        self.parent = None
        self.children = []

class BTree:
    def __init__(self, node: Node = None, scala=3):
        self.root = Node(scala=scala)
        self.scala = scala
        self.mid_index = int((self.scala - 1) / 2)

    def _find(self, value, node: Node = None):
        if not node:
            return BTree.compare(value, self.root)
        else:
            return BTree.compare(value, node)

    def _split(self, node):
        if len(node.values) <= self.scala - 1:
            return 0

        parent = node.parent
        new_node, l_node, r_node = Node(), Node(), Node()

        mid_index = self.mid_index
        l_node.values = node.values[0:mid_index]
        center = node.values[mid_index]
        r_node.values = node.values[mid_index + 1:]

        if node.children != []:
            l_node.children = node.children[0:mid_index + 1]
            r_node.children = node.children[mid_index + 1:]
            for i in range(mid_index + 1):
                node.children[i].parent = l_node
            for i in range(mid_index + 1, self.scala + 1):
                node.children[i].parent = r_node

        if not parent:
            parent = new_node
            parent.values.append(center)
            parent.children.insert(0, l_node)
            parent.children.insert(1, r_node)
            l_node.parent = parent
            r_node.parent = parent
            self.root = parent
            return 0

        l_node.parent = parent
        r_node.parent = parent
        parent.insert(center)
        index = parent.children.index(node)
        parent.children.pop(index)
        parent.children.insert(index, l_node)
        parent.children.insert(index + 1, r_node)
        return self._split(parent)

    def insert(self, *values):
        for value in values:
            node = self.find(value)
            length = node.insert(value)
            if length == self.scala:
                self._split(node)