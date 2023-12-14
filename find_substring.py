
def max_num(num):
    new_str = ""
    for i in range(len(num)-2):
        sub_str = num[i:i+3]
        for i in range(0,len(num),3):
            if len(set(sub_str)) == 1:
                new_str = max(new_str,sub_str)
    return new_str        
    

            

num = "42352338"

result = max_num(num)

print(result if result else "No substring of length 3 consists of only one unique digit. Therefore, there are no good integers")