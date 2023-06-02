import pytest

from linked_list.linked_list import LinkedList
from linked_list.stacks_and_queues import (Stack, Queue, PseudoQueue, AnimalShelter)

@pytest.mark.skip(reason="Done")
def test_linkedlist_instantiattion_empty():
    new_list = LinkedList()
    actual = (new_list.head == None)
    expected = True
    assert actual == expected

@pytest.mark.skip(reason="Done")
def test_linkedlist_insertion_by_function():
    new_list = LinkedList()
    new_list.insert("Georgia")
    head = new_list.head.value
    actual = head
    expected = "Georgia"
    assert actual == expected

@pytest.mark.skip(reason="Done")
def test_linkedlist_head_points_to_first_node_():
    new_list = LinkedList()
    new_list.insert("London")
    new_list.insert("Paris")
    new_list.insert("Amsterdam")
    new_list.insert("Manila")
    new_list.insert("Tokyo")
    head = new_list.head.value
    actual = head
    expected = "Tokyo"
    assert actual == expected

@pytest.mark.skip(reason="Done")
def test_linkedlist_includes_():
    new_list = LinkedList()
    new_list.insert("Berlin")
    new_list.insert("Istanbul")
    new_list.insert("Zegreb")
    assert new_list.includes("Berlin") == True
    assert new_list.includes("Moscow") == False

@pytest.mark.skip(reason="Done")
def test_linkedlist_to_string_():
    new_list = LinkedList()
    new_list.insert("C")
    new_list.insert("B")
    new_list.insert("A")
    assert new_list.to_string() == "{ A } -> { B } -> { C } -> None"

#####################################
#############  Class 06 #############
#####################################

@pytest.mark.skip(reason="Done")
def test_linkedlist_append():
    new_list = LinkedList()
    new_list.insert("2")
    new_list.insert("3")
    new_list.insert("1")
    new_list.append("5")
    assert new_list.to_string() == "{ 1 } -> { 3 } -> { 2 } -> { 5 } -> None"
    new_list2 = LinkedList()
    new_list2.append("1")
    assert new_list2.to_string() == "{ 1 } -> None"

@pytest.mark.skip(reason="Done")
def test_linkedlist_insert_before():
    new_list = LinkedList()
    new_list.insert("2")
    new_list.insert("3")
    new_list.insert("1")
    new_list.insert_before("3", "5")
    assert new_list.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 2 } -> None"

    new_list2 = LinkedList()
    new_list2.insert("2")
    new_list2.insert("3")
    new_list2.insert("1")
    new_list2.insert_before("1", "5")
    assert new_list2.to_string() == "{ 5 } -> { 1 } -> { 3 } -> { 2 } -> None"

    new_list3 = LinkedList()
    new_list3.insert("2")
    new_list3.insert("2")
    new_list3.insert("1")
    new_list3.insert_before("2", "5")
    assert new_list3.to_string() == "{ 1 } -> { 5 } -> { 2 } -> { 2 } -> None"

    new_list4 = LinkedList()
    new_list4.insert("2")
    new_list4.insert("3")
    new_list4.insert("1")
    new_list4.insert_before("4", "5")
    assert new_list4.to_string() == "{ 1 } -> { 3 } -> { 2 } -> None"


@pytest.mark.skip(reason="Done")
def test_linkedlist_insert_after():
    new_list = LinkedList()
    new_list.insert("2")
    new_list.insert("3")
    new_list.insert("1")
    new_list.insert_after("3", "5")
    assert new_list.to_string() == "{ 1 } -> { 3 } -> { 5 } -> { 2 } -> None"

    new_list2 = LinkedList()
    new_list2.insert("2")
    new_list2.insert("3")
    new_list2.insert("1")
    new_list2.insert_after("2", "5")
    assert new_list2.to_string() == "{ 1 } -> { 3 } -> { 2 } -> { 5 } -> None"

    new_list3 = LinkedList()
    new_list3.insert("2")
    new_list3.insert("2")
    new_list3.insert("1")
    new_list3.insert_after("2", "5")
    assert new_list3.to_string() == "{ 1 } -> { 2 } -> { 5 } -> { 2 } -> None"

    new_list4 = LinkedList()
    new_list4.insert("2")
    new_list4.insert("3")
    new_list4.insert("1")
    new_list4.insert_after("4", "5")
    assert new_list4.to_string() == "{ 1 } -> { 3 } -> { 2 } -> None"

#####################################
#############  Class 07 #############
#####################################

@pytest.mark.skip(reason="Done")
def test_linkedlist_kthFromEnd_zero():
    new_list = LinkedList()
    new_list.insert("1")
    new_list.insert("3")
    new_list.insert("8")
    new_list.insert("2")
    assert new_list.kthFromEnd(0) == "2"

@pytest.mark.skip(reason="Done")
def test_linkedlist_kthFromEnd_two():
    new_list2 = LinkedList()
    new_list2.insert("1")
    new_list2.insert("3")
    new_list2.insert("8")
    new_list2.insert("2")
    assert new_list2.kthFromEnd(2) == "3"

@pytest.mark.skip(reason="Done")
def test_linkedlist_kthFromEnd_three():
    new_list3 = LinkedList()
    new_list3.insert("1")
    new_list3.insert("3")
    new_list3.insert("8")
    new_list3.insert("2")
    assert new_list3.kthFromEnd(3) == "1"

@pytest.mark.skip(reason="Done")
def test_linkedlist_kthFromEnd_negative():
    new_list3 = LinkedList()
    new_list3.insert("1")
    new_list3.insert("3")
    new_list3.insert("8")
    new_list3.insert("2")
    assert new_list3.kthFromEnd(-1) == "1"

@pytest.mark.skip(reason="Done")
def test_linkedlist_kthFromEnd_six():
    new_list4 = LinkedList()
    new_list4.insert("1")
    new_list4.insert("3")
    new_list4.insert("8")
    new_list4.insert("2")
    assert new_list4.kthFromEnd(6) == "3"

@pytest.mark.skip(reason="Done")
def test_linkedlist_kthFromEnd_size_of_one():
    new_list5 = LinkedList()
    new_list5.insert("2")
    assert new_list5.kthFromEnd(0) == "2"


#####################################
#############  Class 10 #############
#####################################

#############   Stacks  #############

@pytest.mark.skip(reason="Done")
def test_stacks_instantiation():
    new_stack = Stack()
    assert new_stack.top == None

@pytest.mark.skip(reason="Done")
def test_stacks_push_one():
    new_stack = Stack()
    new_stack.push("Hello")
    assert new_stack.top.value == "Hello"

@pytest.mark.skip(reason="Done")
def test_stacks_push_two():
    new_stack = Stack()
    new_stack.push("Hello")
    new_stack.push("World")
    new_stack.push("Testing")
    assert new_stack.top.value == "Testing"

@pytest.mark.skip(reason="Done")
def test_stacks_pop():
    new_stack = Stack()
    new_stack.push("Red")
    new_stack.push("Orange")
    new_stack.push("Green")
    new_stack.push("Blue")
    new_stack.push("Gray")

    assert new_stack.pop() == "Gray"
    assert new_stack.top.value == "Blue"

@pytest.mark.skip(reason="Done")
def test_stacks_multiple_pops():
    new_stack = Stack()
    new_stack.push("Red")
    new_stack.push("Orange")
    new_stack.push("Green")
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    # new_stack.pop() # Uncomment to check if pop method raises an error when called on an empty stack
    assert new_stack.top == None

@pytest.mark.skip(reason="Done")
def test_stacks_peek():
    new_stack = Stack()
    # new_stack.peek() # Uncomment to check if peek method raises an error when called on an empty stack
    new_stack.push("Germany")
    new_stack.push("Netherlands")
    new_stack.push("Belgium")
    assert new_stack.peek() == 'Belgium'
    new_stack.pop()
    assert new_stack.peek() == 'Netherlands'

@pytest.mark.skip(reason="Done")
def test_stacks_empty():
    new_stack = Stack()
    assert new_stack.is_empty() == True

#############   Queues  #############

@pytest.mark.skip(reason="Done")
def test_queues_instantiation():
    new_queue = Queue()
    assert new_queue.back == None
    assert new_queue.front == None

@pytest.mark.skip(reason="Done")
def test_queues_enqueue():
    new_queue = Queue()
    new_queue.enqueue("Red")
    new_queue.enqueue("Blue")
    assert new_queue.back.value == "Blue"
    assert new_queue.front.value == "Red"

@pytest.mark.skip(reason="Done")
def test_queues_dequeue():
    new_queue = Queue()
    new_queue.enqueue("Red")
    new_queue.enqueue("Blue")
    assert new_queue.front.value == "Red"
    assert new_queue.dequeue() == "Red"
    assert new_queue.front.value == "Blue"
    assert new_queue.back.value == "Blue"

@pytest.mark.skip(reason="Done")
def test_queues_multiple_dequeues():
    new_queue = Queue()
    new_queue.enqueue("Red")
    new_queue.enqueue("Blue")
    new_queue.dequeue()
    new_queue.dequeue()
    # new_queue.dequeue() # Uncomment to check if dequeue method raises an error when called on an empty Queue
    assert new_queue.is_empty() == True

@pytest.mark.skip(reason="Done")
def test_queues_peek():
    new_queue = Queue()
    # assert new_queue.peek() # Uncomment to check if peek method raises an error when called on an empty Queue
    new_queue.enqueue("Jordan")
    new_queue.enqueue("Egypt")
    new_queue.enqueue("Turkey")
    assert new_queue.peek() == "Jordan"

@pytest.mark.skip(reason="Done")
def test_queues_instantiation():
    new_queue = Queue()
    assert new_queue.is_empty() == True

#############   Zip Lists  #############

@pytest.mark.skip(reason="Done")
def test_zip_lists_one():
    ll1 = LinkedList()
    ll1.insert("2")
    ll1.insert("3")
    ll1.insert("1")
    ll2 = LinkedList()
    ll2.insert("4")
    ll2.insert("9")
    ll2.insert("5")
    ll3 = LinkedList.zip_lists(ll1,ll2)
    assert ll3.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> None"

@pytest.mark.skip(reason="Done")
def test_zip_lists_two():
    ll1 = LinkedList()
    ll1.insert("3")
    ll1.insert("1")
    ll2 = LinkedList()
    ll2.insert("4")
    ll2.insert("9")
    ll2.insert("5")
    ll3 = LinkedList.zip_lists(ll1,ll2)
    assert ll3.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> None"

@pytest.mark.skip(reason="Done")
def test_zip_lists_three():
    ll1 = LinkedList()
    ll1.insert("2")
    ll1.insert("3")
    ll1.insert("1")
    ll2 = LinkedList()
    ll2.insert("9")
    ll2.insert("5")
    ll3 = LinkedList.zip_lists(ll1,ll2)
    assert ll3.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> None"

@pytest.mark.skip(reason="Done")
def test_zip_lists_one_list_empty():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll2.insert("9")
    ll2.insert("5")
    ll2.insert("1")
    ll3 = LinkedList.zip_lists(ll1,ll2)
    assert ll3.to_string() == "{ 1 } -> { 5 } -> { 9 } -> None"

@pytest.mark.skip(reason="Done")
def test_zip_lists_both_list_empty():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll3 = LinkedList.zip_lists(ll1,ll2)
    assert ll3.to_string() == "{  } -> None" # this test raises an exception

#############   Pseudo Queue   #############


@pytest.mark.skip(reason="Done")
def test_Pseudo_Queues_instantiation():
    new_queue = PseudoQueue()
    assert new_queue.enqueue_to_stack.top == None
    assert new_queue.dequeue_from_stack.top == None

@pytest.mark.skip(reason="Done")
def test_Pseudo_Queues_enqueue_one():
    new_queue = PseudoQueue()
    new_queue.enqueue("5")
    assert new_queue.enqueue_to_stack.peek() == ("5")

@pytest.mark.skip(reason="Done")
def test_Pseudo_Queues_multiple_enqueue():
    new_queue = PseudoQueue()
    new_queue.enqueue("20")
    new_queue.enqueue("15")
    new_queue.enqueue("10")
    new_queue.enqueue("5")
    assert new_queue.enqueue_to_stack.peek() == ("5")

@pytest.mark.skip(reason="Done")
def test_Pseudo_Queues_multiple_dequeue_one():
    new_queue = PseudoQueue()
    new_queue.enqueue("20")
    new_queue.enqueue("15")
    new_queue.enqueue("10")
    new_queue.enqueue("5")
    assert new_queue.dequeue() == ("20")

@pytest.mark.skip(reason="Done")
def test_Pseudo_Queues_multiple_dequeue_two():
    new_queue = PseudoQueue()
    new_queue.enqueue("15")
    new_queue.enqueue("10")
    new_queue.enqueue("5")
    assert new_queue.dequeue() == ("15")


#############   Animal Shelter   #############

# @pytest.mark.skip(reason="Done")
def test_AnimalShelter_Instanitiation():
    shelter = AnimalShelter()
    assert shelter.dogs.is_empty() == True
    assert shelter.cats.is_empty() == True

# @pytest.mark.skip(reason="Done")
def test_AnimalShelter_Enqueue():
    shelter = AnimalShelter()
    shelter.enqueue({"name":"Rex","species":"dog"})
    assert shelter.dogs.is_empty() == False
    assert shelter.cats.is_empty() == True
    assert shelter.dequeue("dog") == "Rex"

# @pytest.mark.skip(reason="Done")
def test_AnimalShelter_Multiple_Enqueues_and_dequeues():
    shelter = AnimalShelter()
    shelter.enqueue({"name":"Rex","species":"dog"})
    shelter.enqueue({"name":"Macy","species":"cat"})
    shelter.enqueue({"name":"Robby","species":"dog"})
    shelter.enqueue({"name":"Sam","species":"dog"})
    assert shelter.dequeue("dog") == "Rex"
    assert shelter.dequeue("cat") == "Macy"
    assert shelter.dequeue("dog") == "Robby"
    assert shelter.dogs.peek() == "Sam"

@pytest.mark.skip(reason="Done")
def test_AnimalShelter_value_error():
    shelter = AnimalShelter()
    shelter.enqueue({"name":"Loco","species":"bird"})
    assert shelter.dequeue("bird") == "Loco"
    # This test raises Value Error, Unskip it to see the error
    