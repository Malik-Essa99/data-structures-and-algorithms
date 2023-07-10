def insert(sorted_arr, value):
    i = 0
    while i < len(sorted_arr) and value > sorted_arr[i]:
        i += 1
    sorted_arr.append(None)
    j = len(sorted_arr) - 1
    while j > i:
        sorted_arr[j] = sorted_arr[j - 1]
        j -= 1
    sorted_arr[i] = value

def insertion_sort(input_arr):
    sorted_arr = [input_arr[0]]
    for i in range(1, len(input_arr)):
        insert(sorted_arr, input_arr[i])
    return sorted_arr

