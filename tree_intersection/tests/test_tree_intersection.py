from ..tree_intersection import(tree_intersection,Node,Tnode,Tree,Stack,Queue,LinkedList,HashTable,BinarySearch) 

def test_tree_intersection_one():
    tree = BinarySearch()
    tree2 = BinarySearch()
    
    tree.root = Tnode("10")
    tree.root.left = Tnode("20")
    tree.root.right = Tnode("50")
    tree.root.left.left = Tnode("30")

    tree2.root = Tnode("10")
    tree2.root.left = Tnode("20")
    tree2.root.right = Tnode("50")
    tree2.root.left.left = Tnode("30")
    tree2.root.left.right = Tnode("40")
    tree2.root.left.right.left = Tnode("70")
    
    assert  tree_intersection(tree,tree2) == ['30', '20', '10', '50']

def test_tree_intersection_two():
    tree = BinarySearch()
    tree2 = BinarySearch()
    
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
    
    tree2.root = Tnode("42")
    tree2.root.left = Tnode("100")
    tree2.root.right = Tnode("600")
    tree2.root.left.left = Tnode("15")
    tree2.root.left.right = Tnode("160")
    tree2.root.left.right.left = Tnode("125")
    tree2.root.left.right.right = Tnode("175")
    tree2.root.right.left = Tnode("200")
    tree2.root.right.right = Tnode("350")
    tree2.root.right.right.left = Tnode("4")
    tree2.root.right.right.right = Tnode("500")
    
    assert  tree_intersection(tree,tree2) == ["100","125","160","175","200","350","500"]
                                            

def test_tree_intersection_three():
    tree = BinarySearch()
    tree2 = BinarySearch()
    
    tree.root = Tnode("A")
    tree.root.left = Tnode("B")
    tree.root.right = Tnode("C")
    tree.root.left.left = Tnode("D")
    tree.root.left.right = Tnode("E")
    tree.root.right.left = Tnode("F")
    
    tree2.root = Tnode("A")
    tree2.root.left = Tnode("B")
    tree2.root.right = Tnode("D")
    tree2.root.left.left = Tnode("X")
    tree2.root.left.right = Tnode("E")
    tree2.root.right.left = Tnode("F")
    tree2.root.right.left.left = Tnode("L")
    
    assert  tree_intersection(tree,tree2) == ['B', 'E', 'A', 'F', 'D']