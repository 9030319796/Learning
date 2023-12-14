def native_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1



# Binary search

def binary_search(l,target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1    
    middle = (low + high) // 2


    if l[middle] == target:
        return middle
    
    elif target < l[middle]:
        return binary_search(l,target, low, middle-1)
    else:
        return binary_search(l,target, middle+1, high)
    
    


if __name__== '__main__':
    list1 = [80,90,20,23,45]

    target = 20

    print(native_search(list1,target))
    print(binary_search(list1,target))