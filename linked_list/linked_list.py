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
        item_lst=[]
        result = ""
        current = self.head
        
        while current != None:
            item_lst.insert(0,current.value)
            current = current.next

        for item in item_lst:
            result = result + "{" + f" {item} " + "}" + " -> "
        result = result + "None"
        # return item_lst
        return result

    def includes(self, item):
        search_result = False
        current = self.head
        while current != None:
            if current.value == item:
                search_result = True
            current = current.next
        return search_result

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


if __name__ == "__main__":
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
    new_list = LinkedList()
    new_list.insert("A")
    new_list.insert("B")
    new_list.insert("C")
    print(new_list.to_string())
