# class Node:
#     def __init__(self, value, _next=None):
#         self.value = value
#         self.next = _next


# ############# LinkedList #############


# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head
    
#     def includes(self, item):
#         search_result = False
#         current = self.head
#         while current is not None:
#             if current.value == item:
#                 search_result = True
#             current = current.next
#         return search_result
    
#     def append(self, value):
#         if self.head is None:
#             self.insert(value)
#             return
#         new_node = Node(value)
#         current = self.head
#         while current is not None:
#             if current.next is None:
#                 current.next = new_node
#                 new_node.next = None
#             current = current.next

# def find_counter(linked_list1,linked_list2):
#     current = linked_list1.head
#     while current:
#         pass
#         # if current.value ==
    
# if __name__ == "__main__":
#     ll1 = LinkedList
#     ll2 = LinkedList
#     ll1.append(1)
#     ll1.append(3)
#     ll1.append(7)
#     ll1.append(5)
#     ll1.append(1)
# # ll2 values
#     ll2.append(1)
#     ll2.append(3)
#     ll2.append(4)
#     ll2.append(5)
#     ll2.append(1)
#     print(find_counter(ll1,ll2))
