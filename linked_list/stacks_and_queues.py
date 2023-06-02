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
    
    def enqueue(self,animal):
        if animal["species"] == "dog":
            self.dogs.enqueue(animal["name"])
        elif animal["species"] == "cat":
            self.cats.enqueue(animal["name"])
        else:
            raise ValueError("Shelter is only for cats or dogs") 

    def dequeue(self,pref = None):
        if pref == "dog":
            return self.dogs.dequeue()
        elif pref == "cat":
            return self.cats.dequeue()
        else:
            return pref


if __name__ == "__main__":
    pass

    # shelter = AnimalShelter()
    # shelter.enqueue({"name":"Rex","species":"dog"})
    # shelter.enqueue({"name":"Suzie","species":"cat"})
    # shelter.enqueue({"name":"Sherry","species":"cat"})
    # print(shelter.dequeue("dog"))
    # print(shelter.dequeue("cat"))
    # new_queue = PseudoQueue()
    # new_queue.enqueue_to_stack("Hello")
    # print(new_queue.enqueue_to_stack.top.value)