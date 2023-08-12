from stacks_and_queues import (Queue, Stack)

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
    
    def find_max(self):
        ### Recursive ### Using pre order ###
        '''
        this function creates a helper(_walk), and an empty values array,
        then it will call the _walk function and pass the root as args,
        there are two base cases(if there are any left or right for a given root)
        it will add each Tree node value to the values list and then create max,
        Iterate through values and check if they are greater than the max,
        and finally return max
        '''
        if self.root is None:
            raise ValueError("Tree is empty")
        
        values = []
        def _walk(root):
            values.append(root.value)

            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        
        max = values[0]
        if values:
            for num in values:
                if num > max:
                    max = num
        return max
    
        ### Iterative ### Using Breadth First ###

        # if self.root is None:
        #     raise ValueError("Tree is empty")
        
        # values = []
        # stack = Stack()
        # stack.push(self.root)


        # while not stack.is_empty():
        #     top = stack.pop()
        #     values.append(top.value)

        #     if top.left is not None:
        #         stack.push(top.left)

        #     if top.right is not None:
        #         stack.push(top.right)

        # if values[0] is not None:       
        #     max = values[0]
        #     for i in values:
        #         if i > max:
        #             max = i
        # return max

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
        
def compare_trees(tree1, tree2):
    '''Assuming we have access to queue class and its methods,
    first we will create another function breadth_first(),
    that traverses a tree and counts the number of leaves for
    the passed tree, and called for both trees, and finally
    compare the two leaves count and return boolean
    '''
    def breadth_first_compare(tree):
        leaves = 0
        queue = Queue()
        queue.enqueue(tree.root)

        while not queue.is_empty():
            front = queue.dequeue()
            if not front.left and not front.right:
                leaves = leaves + 1
            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
        return leaves

    tree_1_leaves = breadth_first_compare(tree1)
    tree_2_leaves = breadth_first_compare(tree2)
    
    if tree_1_leaves == tree_2_leaves:
        return True
    else:
        return False
    
# def binary_tree_height(tree):
#     root = tree.root
#     if not root:
#         raise ValueError("tree is empty")
    
#     def _helper(root):
#         if root.left or root.right:
#             return 1 + (_helper(root.left) +( _helper(root.right)))
#         return
#         # if root.left:
#         #     _helper(root.left)
#         # if root.right:
#         #     _helper(root.right)

#     return _helper(root)

def binary_tree_height(tree):
    root = tree.root
    if not root:
        return 0

    def _helper(node):
        if not node:
            return 0

        left_height = _helper(node.left)
        right_height = _helper(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
        
    return _helper(root) + 1

if __name__ == "__main__":
    # tree = Tree()
    # tree2 = Tree()
    # tree.root = Tnode("A")
    # tree.root.left = Tnode("B")
    # tree.root.right = Tnode("C")
    # tree.root.left.left = Tnode("D")
    # tree.root.left.right = Tnode("E")
    # tree.root.right.left = Tnode("F")

    # tree.root = Tnode(10)
    # tree.root.left = Tnode(20)
    # tree.root.right = Tnode(50)
    # tree.root.left.left = Tnode(30)
    # tree.root.left.right = Tnode(40)
    # tree.root.right.left = Tnode(60)
    # tree.root.right.left.right = Tnode(70)
    # tree.root.right.left.left = Tnode(90)
    # tree.root.right.left.left.left = Tnode(100)
    # tree.root.right.left.left.left.right = Tnode(100)

    # tree2.root = Tnode(10)
    # tree2.root.left = Tnode(20)
    # tree2.root.right = Tnode(50)
    # tree2.root.left.left = Tnode(30)
    # tree2.root.left.right = Tnode(40)
    # tree2.root.right.left = Tnode(60)
    # tree2.root.right.left.right = Tnode(70)
    # print(tree.find_max())
    # print(compare_trees(tree,tree2))

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
    # print(tree.pre_order())
    # print(" ")
    # print(tree.in_order())
    # print(" ")
    # print(tree.post_order())
    # tree.add("7")
    # print(tree.root.right.right.left.value)
    # print(tree.root.left.left.left.value)
    # print(tree.root.left.right.left.left.value)
    # print(BinarySearch.contains(tree,0))

##################### Tree practice #####################

    tree = Tree()
    tree2 = Tree()
    
    tree.root = Tnode("150")
    tree.root.left = Tnode("100")
    tree.root.right = Tnode("250")
    tree.root.left.left = Tnode("75")
    tree.root.left.right = Tnode("160")
    tree.root.left.right.left = Tnode("125")
    tree.root.left.right.right = Tnode("175")
    tree.root.right.left = Tnode("200")
    tree.root.right.right = Tnode("350")
    tree.root.right.right.left = Tnode("300")
    tree.root.right.right.right = Tnode("500")
    
    # tree2.root = Tnode("42")
    # tree2.root.left = Tnode("100")
    # tree2.root.right = Tnode("600")
    # tree2.root.left.left = Tnode("15")
    # tree2.root.left.right = Tnode("160")
    # tree2.root.left.right.left = Tnode("125")
    # tree2.root.left.right.right = Tnode("175")
    # tree2.root.right.left = Tnode("200")
    # tree2.root.right.right = Tnode("350")
    # tree2.root.right.right.left = Tnode("4")
    # tree2.root.right.right.right = Tnode("500")
    
    print(binary_tree_height(tree))