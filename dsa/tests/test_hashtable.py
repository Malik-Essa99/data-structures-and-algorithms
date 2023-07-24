import pytest 
from dsa.hashtable import HashTable,repeated_word

@pytest.mark.skip(reason="Done")
def test_hash_method():
    hash = HashTable()
    actual = hash._HashTable__hash('d')
    assert 652 == actual

@pytest.mark.skip(reason="Done")
def test_set_method():
    hash = HashTable()
    hash.set("A","Hello")
    # assert hash.has("A")
    assert hash.get("A") == "Hello"

@pytest.mark.skip(reason="Done")
def test_get_method():
    hash = HashTable()
    hash.set("A","Hello")
    hash.set("B","Good morning")
    assert hash.get("A") == "Hello"

@pytest.mark.skip(reason="Done")
def test_has_method():
    hash = HashTable()
    hash.set("A","Orange")
    hash.set("B","Apple")
    assert hash.has("B") == True
    assert hash.has("C") == False

@pytest.mark.skip(reason="Done")
def test_return_none_for_no_existing_key():
    hash = HashTable()
    hash.set("1","Rock")
    assert hash.get("1") == "Rock"
    assert hash.get("2") == None

@pytest.mark.skip(reason="Done")
def test_all_keys():
    hash = HashTable()
    hash.set("1","Rock")
    hash.set("A","Rock")
    hash.set("#","Rock")
    assert hash.keys == ["1","A","#"]
    assert hash.keys != ["1","A","#","H","U"]

@pytest.mark.skip(reason="Done")
def test_collision_handling():
    hash = HashTable()
    hash.set("12","Rock")
    assert hash.get("12") == "Rock"
    hash.set("1","Paper")
    assert hash.get("1") == "Paper"
    hash.set("1","scissors")
    assert hash.get("1") == "scissors"

################ Challenge 31 ################

# @pytest.mark.skip(reason="Done")
def test_collision_handling():
    string = "Once upon a time, there was a brave princess who..."
    string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

    assert repeated_word(string) == "a"
    assert repeated_word(string2) == "it"
    assert repeated_word(string3) == "summer"