# Merge Sort
### Author: Malik Al Hudrub
### How to initialize/run your application:
python data-structures-and-algorithms/Merge-Sort/Insertion_sort.py

### Testing 
### How do you run tests?
+ cd data-structures-and-algorithms/Merge-Sort/tests 
+ pytest tests.py

### Algorithm:

``` 
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```
### Test cases visualization:

Case 1:
![one]()
Case 2:
![two]()
Case 3:
![three]()
Case 4:
![four]()


### Efficency:
Time: O()
+ 

Space: O()
+ 