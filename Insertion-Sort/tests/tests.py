from Insertion_sort import insertion_sort

def test_insertion_one():
    arr = [8,4,23,42,16,15]
    sorted_arr = insertion_sort(arr)
    assert sorted_arr == [4,8,15,16,23,42]
    
def test_insertion_two():
    arr = [20,18,12,8,5,-2]
    sorted_arr = insertion_sort(arr)
    assert sorted_arr == [-2,5,8,12,18,20]
    
def test_insertion_three():
    arr = [5,12,7,5,5,7]
    sorted_arr = insertion_sort(arr)
    assert sorted_arr == [5,5,5,7,7,12]
    
def test_insertion_four():
    arr = [2,3,5,7,13,11]
    sorted_arr = insertion_sort(arr)
    assert sorted_arr == [2,3,5,7,11,13]
    
