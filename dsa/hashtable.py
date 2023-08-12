import re
class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

class HashTable:
    def __init__(self,size = 1024):
        self.__size = size
        self.__buckets = [None] * size
        self.keys = []

    def __hash(self,key):
        # code = 0

        # for char in key:
        #     code += ord(str(char))
        #     code *= 599
        #     code = code % 1024

        # return code
        
        # return (sum([ord(str(key)) for char in key]) * 283 % 1024) # this function only hashes if the string had 1 char
        return sum([ord(char) for char in key]) * 283 % self.__size

    def set(self,key,value):
        index = self.__hash(key)
        if self.__buckets[index] is None:
            ll = LinkedList()
            self.__buckets[index] = ll

        self.__buckets[index].insert([key,value])
        self.keys.append(key)

    def get(self,key):
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket is not None:
            curr = bucket.head
            while curr:
                if curr.value[0] == key:
                    return curr.value[1]
                curr = curr.next
        return None
    
    def has(self,key):
        # index = self.__hash(key)
        # bucket = self.__buckets[index]
        # if bucket is not None:
        #     curr = bucket.head
        #     while curr:
        #         if curr.value[0] == key:
        #             return True
        #         curr = curr.next
        #     return False
        if self.get(key):
            return True
        return False
    
    def keys(self):
        return self.keys

def repeated_word(_str):
    clean_str = re.sub(r"[^a-zA-Z\s]", "", _str)
    words = clean_str.lower().split(" ")
    hash = HashTable()
    
    for word in words:
        if hash.has(word):
            return word
        else:
            hash.set(word, "added")
    return ("there are no duplicates")

def left_joins(hashmap1,hashmap2):
    if not hashmap2.keys and not hashmap1.keys:
        raise "Both hashtables are empty"
    
    keys1 = hashmap1.keys
    all_keys = []
    
    for key in keys1:
        if key not in all_keys:
            all_keys.append(key)
    
    result = []
    for key in all_keys:
        set = []
        set.append(key)
        if hashmap1.has(key):
            set.append(hashmap1.get(key))
        else:
            set.append(None)

        if  hashmap2.has(key):
            set.append(hashmap2.get(key))
        else:
            set.append(None)
            
        result.append(set)
    return result

if __name__=="__main__":
    
    ################### Repeated Word  ###################
    
    # hash = HashTable()
    # string = "Once upon a time, there was a brave princess who..."
    # string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    # string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    # print(repeated_word(string))
    # print(repeated_word(string2))
    # print(repeated_word(string3))
    
    ################### Left Joins ###################
    
    
    
    hash_synonym  = HashTable()
    hash_antonyms = HashTable()
    # arr = {
    # "font": {"synonym": "enamored", "antonyms": "averse"},
    # "wrath": {"synonym": "anger", "antonyms": "delight"},
    # "diligent": {"synonym": "employed", "antonyms": "idle"},
    # "outfit": {"synonym": "garb", "antonyms": None},
    # "guide": {"synonym": "usher", "antonyms": "follow"}
    # }
    # for key,value in arr.items():
    #     hash_synonym.set(key,value["synonym"])
    #     hash_antonyms.set(key,value["antonyms"])

    hash_synonym.set("diligent","employed")
    hash_antonyms.set("diligent","idle")
    
    hash_synonym.set("fond","enamored")
    hash_antonyms.set("fond","averse")
    
    hash_synonym.set("guide","usher")
    hash_antonyms.set("guide","follow")
    
    hash_synonym.set("outfit","garb")
    hash_antonyms.set("flow","jam")
    
    hash_synonym.set("wrath","anger")
    hash_antonyms.set("wrath","delight")
    
    print(left_joins(hash_synonym,hash_antonyms))