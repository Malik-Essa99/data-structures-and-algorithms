test = [[2,4,6,-8], 5]
test2 = [[42,8,15,23,42], 16]
def array_insert_shift(lst):
    arr = lst[0]
    num = lst[1]
    result =[]
    if len(arr)%2 ==0:  
        for i in range(len(arr)):
        
            if i == len(arr)//2:
                result.append(num)
            result.append(arr[i])
    else:
        for i in range(len(arr)):
            if i == 1 +  len(arr)//2:
                result.append(num)
            result.append(arr[i])
    print(result)
array_insert_shift(test)    
array_insert_shift(test2)