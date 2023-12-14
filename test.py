import re

def find_substring(num):
    max_good = ""
    for i in range(len(num)-2):
        substr = num[i:i+3]
        if len(set(substr)) == 1:
            max_good = substr
            
    return max_good if max_good else "None"
             
num = "42352338"

result = find_substring(num)

print(f"Maximum good integer is {result}")


