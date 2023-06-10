from stacks_and_queues import Queue

class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class Tnode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def breadth_first(self):
        if not self.root:
            return self.root

        output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            front = queue.dequeue()
            output.append(front.value)

            if front.left is not None:
                queue.enqueue(front.left)

            if front.right is not None:
                queue.enqueue(front.right)

        return output

    def pre_order(self):
        output = []

        def _walk(root):
            output.append(root.value)

            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def in_order(self):
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            output.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def post_order(self):
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

            output.append(root.value)

        _walk(self.root)
        return output


class BinarySearch(Tree):
    def contains(self, value):
        try:
            is_found = False
            root = self.root

            while root is not None:
                if value == root.value:
                    is_found = True
                    return is_found

                if value < root.value:
                    root = root.left
                else:
                    root = root.right
            return is_found
        except TypeError:
            raise ValueError("Value must be a number!")
        
    def add(self,value):

        if self.contains(value):
            raise ValueError("The value is already in the Tree!")
        
        if self.root is None:
            self.root = Tnode(value)
            return
        
        root = self.root
        while root is not None:
            if value < root.value:
                if root.left is None:
                    root.left = Tnode(value)
                    return
                root = root.left

            elif value > root.value:
                if root.right is None:
                    root.right = Tnode(value)
                    return
                root = root.right

if __name__ == "__main__":
    tree = Tree()
    tree.root = Tnode("A")
    tree.root.left = Tnode("B")
    tree.root.right = Tnode("C")
    tree.root.left.left = Tnode("D")
    tree.root.left.right = Tnode("E")
    tree.root.right.left = Tnode("F")

    # tree.root = Tnode(10)
    # tree.root.left = Tnode(20)
    # tree.root.right = Tnode(50)
    # tree.root.left.left = Tnode(30)
    # tree.root.left.right = Tnode(40)
    # tree.root.right = Tnode(50)
    # tree.root.right.left = Tnode(60)

    # tree.root = Tnode(23)
    # tree.root.left = Tnode(8)
    # tree.root.left.left = Tnode(4)
    # tree.root.left.right = Tnode(16)
    # tree.root.left.right.left = Tnode(15)
    # tree.root.left.right.right = Tnode(22)

    # tree.root.right = Tnode(42)
    # tree.root.right.left = Tnode(27)
    # tree.root.right.right = Tnode(85)
    # tree.root.right.right.right= Tnode(105)
    # print(tree.add(30))
    # print(tree.add(30))
    # tree.add(30)
    # tree.add(39)
    # tree.add(41)
    # tree.add(43)
    # tree.add(79)
    # tree.add(9)
    # tree.add(28)

    # print(tree.breadth_first())
    print(tree.pre_order())
    print(" ")
    print(tree.in_order())
    print(" ")
    print(tree.post_order())
    # tree.add("7")
    # print(tree.root.right.right.left.value)
    # print(tree.root.left.left.left.value)
    # print(tree.root.left.right.left.left.value)
    # print(BinarySearch.contains(tree,0))
