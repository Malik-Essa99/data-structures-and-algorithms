class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


############# LinkedList #############


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    @staticmethod
    def reverse_linkedlist(ll_1):
        current = ll_1.head
        temp_list = []
        counter = 0
        new_list = LinkedList()

        while current:
            temp_list[counter] = current.value
            current = current.next
            counter +=1
        if counter == 0:
            return (new_list)

        for i in temp_list:
            new_node = Node(i)
            new_node.next = new_list.head
            new_list.head = new_node
        return (new_list)

if __name__ == "__main__":

    ll = LinkedList()
    node_1 = Node("1")
    node_2 = Node("2")
    node_3 = Node("1")
    print(LinkedList.reverse_linkedlist(ll))
