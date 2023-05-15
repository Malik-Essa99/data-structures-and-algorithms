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
    new_list.insert("C")
    new_list.insert("B")
    new_list.insert("A")
    assert new_list.to_string() == "{ A } -> { B } -> { C } -> None"

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
