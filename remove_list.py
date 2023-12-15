def remove(nums,val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i+=1
    return i
    
nums = [1,2,2,3,3,4,4,5,5]
val = 2

k = remove(nums,val)

print("New array:", nums[:k])
print("Number of elements not equal to val:", k)
