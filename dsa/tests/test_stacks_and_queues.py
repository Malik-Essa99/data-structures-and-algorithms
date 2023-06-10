import pytest
from dsa.stacks_and_queues import (Stack, Queue, PseudoQueue, AnimalShelter, validate_brackets)

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

@pytest.mark.skip(reason="Done")
def test_AnimalShelter_Instanitiation():
    shelter = AnimalShelter()
    assert shelter.dogs.is_empty() == True
    assert shelter.cats.is_empty() == True

@pytest.mark.skip(reason="Done")
def test_AnimalShelter_Enqueue():
    shelter = AnimalShelter()
    shelter.enqueue({"name":"Rex","species":"dog"})
    assert shelter.dogs.is_empty() == False
    assert shelter.cats.is_empty() == True
    assert shelter.dequeue("dog") == "Rex"

@pytest.mark.skip(reason="Done")
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

@pytest.mark.skip(reason="Done")
def test_validate_brackets_one():
    str1 = "{}"
    str2 = "{}(){}"
    str3 = "()[[Extra Characters]]"
    str4 = "(){}[[]]"
    str5 = "{}{Code}[Fellows](())"
    str6 = "[({}]"
    str7 = "(]("
    str8 = "{(})"
    str9 = "{"
    str10 = "}"
    str11 = "{)"
    assert validate_brackets(str1) == True
    assert validate_brackets(str2) == True
    assert validate_brackets(str3) == True
    assert validate_brackets(str4) == True
    assert validate_brackets(str5) == True
    assert validate_brackets(str6) == False
    assert validate_brackets(str7) == False
    assert validate_brackets(str8) == False
    assert validate_brackets(str9) == False
    assert validate_brackets(str10) == False
    assert validate_brackets(str11) == False