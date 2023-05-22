class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


############# LinkedList #############


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

    def insert_before(self, target, new_value):
        current = self.head
        while current is not None:
            if current.next.value == target:
                new_node = Node(new_value, current.next)
                current.next = new_node
                current = current.next
            elif self.head.value == target:
                self.insert(new_value)
            else:
                self.to_string()
            return

    def insert_after(self, target, new_value):
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

    def kthFromEnd(self, k):
        try:
            temp_lst = []
            current = self.head
            while current != None:
                temp_lst.append(current.value)
                current = current.next
            # print(temp_lst)
            if k <= len(temp_lst):
                return temp_lst[k]
            else:
                raise ValueError
        except ValueError as ve:
            print(ve)
            raise ValueError(f"Linked list has fewer than {k} elements.")
        
    @staticmethod
    def zip_lists(ll_1,ll_2):
        try:
            if ll_1.head == None and ll_2.head == None:
                raise ValueError
            ll_1_current = ll_1.head
            ll_2_current = ll_2.head
            new_ll = LinkedList()
            while ll_1_current or ll_2_current:
                if ll_1_current is not None:
                    new_ll.append(ll_1_current.value)
                    ll_1_current = ll_1_current.next
                if ll_2_current is not None:
                    new_ll.append(ll_2_current.value)
                    ll_2_current = ll_2_current.next
            return new_ll
        except ValueError as ve:
            print(ve)
            raise ValueError("Both Lists are empty")
            
############# Stack #############


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        try:
            if self.top is not None:
                temp = self.top
                self.top = temp.next
                temp.next = None
                return temp.value
            else:
                raise ValueError

        except ValueError as ve:
            print(ve)
            raise ValueError("Stack is empty")

    def peek(self):
        try:
            if self.top is not None:
                return str(self.top.value)
            else:
                raise ValueError

        except ValueError as ve:
            print(ve)
            raise ValueError(f"Stack is empty")

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False


############# Queues #############


class Queue:
    def __init__(self,back=None ,front=None ):
        self.back = back
        self.front = front

    def enqueue(self,value):
        new_node = Node(value)

        if self.front == None:
            self.back = new_node
            self.front = new_node
            self.back.next = None
            self.front.next = None
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        
        try:
            if self.front is not None:
                temp = self.front
                self.front = temp.next
                temp.next = None
                return temp.value
            else:
                raise ValueError

        except ValueError as ve:
            print(ve)
            raise ValueError("Queue is empty")
        
    def peek(self):
        try:
            if self.front is not None:
                return str(self.front.value)
            else:
                raise ValueError

        except ValueError as ve:
            print(ve)
            raise ValueError(f"Queue is empty")  
          
    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False
        


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
    # new_list = LinkedList()
    # new_list.insert("1")
    # new_list.insert("3")
    # new_list.insert("8")
    # new_list.insert("2")
    # new_list.kthFromEnd(0)
    # new_node = Queue()
    # new_node.enqueue("Hello")
    # print(new_node.front.value)
    # print(new_node.back.value)
    # new_node.enqueue("World")
    # print("-----------")
    # print(new_node.front.value)
    # print(new_node.back.value)
    # print("-----------")
    # new_node.enqueue("Nice")
    # print(new_node.front.value)
    # print(new_node.back.value)
    # new_node = Queue()
    # new_node.enqueue("Hello")
    # print(new_node.front.next)
    # print(new_node.back.next)
    # new_node.enqueue("World")
    # print(new_node.front.next.next)
    # print(new_node.back.next)
    # new_node.enqueue("Nice")
    # print(new_node.front.next.value)
    # print(new_node.back.next)

    ll1 = LinkedList()
    ll1.insert("2")
    ll1.insert("3")
    ll1.insert("1")
    ll2 = LinkedList()
    # ll2.insert("4")
    ll2.insert("9")
    ll2.insert("5")
    # print(ll2.to_string())
    ll3 = LinkedList.zip_lists(ll1,ll2)
    print(ll3.to_string())