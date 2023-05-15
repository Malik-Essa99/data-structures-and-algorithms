class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # def traverse(self):
    #     current = self.head
    #     while current != None:
    #         print(current.value)
    #         current = current.next

    def to_string(self):
        item_lst = []
        result = ""
        current = self.head

        while current != None:
            item_lst.append(current.value)
            current = current.next

        for item in item_lst:
            result = result + "{" + f" {item} " + "}" + " -> "
        result = result + "None"
        return result

    def includes(self, item):
        search_result = False
        current = self.head
        while current is not None:
            if current.value == item:
                search_result = True
            current = current.next
        return search_result

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, value):
        if self.head is None:
            self.insert(value)
            return
        new_node = Node(value)
        current = self.head
        while current is not None:
            if current.next is None:
                current.next = new_node
                new_node.next = None
            current = current.next

    def insert_before(self,target,new_value):
        current = self.head
        while current is not None:
            if current.next.value == target:
                new_node = Node(new_value,current.next)
                new_node.next = current.next
                current.next = new_node
                current = current.next
            elif self.head.value == target:
                self.insert(new_value)
            else:
                self.to_string() 
            return
        
    def insert_after(self,target,new_value):
        current = self.head
        while current is not None:
            if current.value == target and current.next is not None:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            elif current.value == target and current.next == None:
                self.append(new_value)
            current = current.next

            # elif self.head.value == target:
            #     self.insert(new_value)
            # else:
            #     self.to_string() 
            


if __name__ == "__main__":
    pass
    # node_a= Node("A")
    # node_b= Node("B", node_a)
    # print (node_d.value)
    # print (node_h.value,node_h.next.value)
    # node_c= Node("C",node_b)
    # LinkedList(node_d)
    # LinkedList(node_d)
    # LinkedList(node_d)
    # LinkedList(node_d)
    # ll_ = LinkedList(node_c)
    # # ll_.traverse()
    # ll_.insert("D")
    # ll_.traverse()
    # nl_ = LinkedList()
    # print (nl_)
    # print (ll_.head.value)
    # print (ll_.head.next.value)
    # new_list = LinkedList()
    # new_list.insert("A")
    # new_list.insert("B")
    # new_list.insert("C")
    # print(new_list.to_string())
    # new_list2 = LinkedList()
    # new_list2.insert("A")
    # new_list2.insert("B")
    # new_list2.insert("C")
    # new_list2.append("D")
    # print(new_list2.to_string())
    # print(new_list2.head.next.value)
    # new_list2 = LinkedList()
    # new_list2.insert("2")
    # new_list2.insert("3")
    # new_list2.insert("1")
    # new_list2.insert_before("2", "5")
    # assert new_list2.to_string() == "{ 1 } -> { 3 } -> { 2 } -> { 5 } -> None"