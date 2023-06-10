class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


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
                return self.top.value
                
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
    def __init__(self, back=None, front=None):
        self.back = back
        self.front = front

    def enqueue(self, value):
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

class PseudoQueue:
    def __init__(self):
        self.enqueue_to_stack = Stack()
        self.dequeue_from_stack = Stack()

    def enqueue(self, value):
        self.enqueue_to_stack.push(value)

    def dequeue(self):
        if self.dequeue_from_stack.is_empty():
            while not self.enqueue_to_stack.is_empty():
                self.dequeue_from_stack.push(self.enqueue_to_stack.pop())
        return self.dequeue_from_stack.pop()

class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if animal["species"] == "dog":
            self.dogs.enqueue(animal["name"])
        elif animal["species"] == "cat":
            self.cats.enqueue(animal["name"])
        else:
            raise ValueError("Shelter is only for cats or dogs")

    def dequeue(self, pref=None):
        if pref == "dog":
            return self.dogs.dequeue()
        elif pref == "cat":
            return self.cats.dequeue()
        else:
            return pref

def validate_brackets(test_str):
    """ This function will first it will first create a dict and save opening and closing
    brackets as key and value, then it will create a stack and a queue and to save each opening
    and closing bracket in the string, then  it will iterate through the string and check
    if the current index value is inside the keys in the dict, and push it to the stack if True
    and then check if closing brackets are values for the keys, if true
    it will pop and dequeue both the values from stack and queue, and finally check
    if both stack and queue are empty Return True yes and False if no
    """
    targets = {"{":"}", "(":")", "[":"]"}
    opening_char_stack = Stack()
    closing_char_queue = Queue()
    for i in test_str:
        if i in targets.keys():
            opening_char_stack.push(i)
        elif i in targets.values():
            closing_char_queue.enqueue(i)
            try:
                if (closing_char_queue.front.value == targets[opening_char_stack.top.value]):
                    opening_char_stack.pop()
                    closing_char_queue.dequeue()
            except:
                return False
    if opening_char_stack.is_empty() and closing_char_queue.is_empty():
        return True
    else:
        return False

if __name__ == "__main__":
    pass
    # str1 = "{}"
    # str2 = "{}(){}"
    # str3 = "()[[Extra Characters]]"
    # str4 = "(){}[[]]"
    # str5 = "{}{Code}[Fellows](())"
    # str6 = "[({}]"
    # str7 = "(]("
    # str8 = "{(})"
    # str9 = "{"
    # str10 = "}"
    # str11 = "{)"

    # print(validate_brackets(str1))
    # print(validate_brackets(str2))
    # print(validate_brackets(str3))
    # print(validate_brackets(str4))
    # print(validate_brackets(str5))
    # print(validate_brackets(str6))
    # print(validate_brackets(str7))
    # print(validate_brackets(str8))
    # print(validate_brackets(str9))
    # print(validate_brackets(str10))
    # print(validate_brackets(str11))

    # shelter = AnimalShelter()
    # shelter.enqueue({"name":"Rex","species":"dog"})
    # shelter.enqueue({"name":"Suzie","species":"cat"})
    # shelter.enqueue({"name":"Sherry","species":"cat"})
    # print(shelter.dequeue("dog"))
    # print(shelter.dequeue("cat"))
    # new_queue = PseudoQueue()
    # new_queue.enqueue_to_stack("Hello")
    # print(new_queue.enqueue_to_stack.top.value)
