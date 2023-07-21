import pytest 

from dsa.hashtable import HashTable

def test_hash_method():
    hash = HashTable()
    actual = hash._HashTable__hash('d')
    assert 652 == actual

def test_set_method():
    hash = HashTable()
    hash.set("A","Hello")
    # assert hash.has("A")
    assert hash.get("A") == "Hello"

def test_get_method():
    hash = HashTable()
    hash.set("A","Hello")
    hash.set("B","Good morning")
    assert hash.get("A") == "Hello"

def test_has_method():
    hash = HashTable()
    hash.set("A","Orange")
    hash.set("B","Apple")
    assert hash.has("C") == False

def test_return_none_for_no_existing_key():
    hash = HashTable()
    hash.set("1","Rock")
    assert hash.get("1") == "Rock"
    assert hash.get("2") == None

def test_all_keys():
    hash = HashTable()
    hash.set("1","Rock")
    hash.set("A","Rock")
    hash.set("#","Rock")
    assert hash.keys == ["1","A","#"]
    assert hash.keys != ["1","A","#","H","U"]

def test_collision_handling():
    hash = HashTable()
    hash.set("1","Rock")
    assert hash.get("1") == "Rock"
    hash.set("1","Paper")
    assert hash.get("1") == "Paper"
    hash.set("1","scissors")
    assert hash.get("1") == "scissors"