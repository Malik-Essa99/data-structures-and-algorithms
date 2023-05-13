import pytest

from linked_list.linked_list import (
    LinkedList
    )

def test_linkedlist_instantiattion_empty():
    new_list = LinkedList()
    actual = (new_list.head == None)
    expected = True
    assert actual == expected

def test_linkedlist_insertion_by_function():
    new_list = LinkedList()
    new_list.insert("Georgia")
    head = new_list.head.value
    actual = head
    expected = "Georgia"
    assert actual == expected

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

def test_linkedlist_includes_():
    new_list = LinkedList()
    new_list.insert("Berlin")
    new_list.insert("Istanbul")
    new_list.insert("Zegreb")
    assert new_list.includes("Berlin") == True
    assert new_list.includes("Moscow") == False

def test_linkedlist_to_string_():
    new_list = LinkedList()
    new_list.insert("A")
    new_list.insert("B")
    new_list.insert("C")
    assert new_list.to_string() == "{ A } -> { B } -> { C } -> None"
