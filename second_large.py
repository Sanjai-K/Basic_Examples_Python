#Python code to find second largest number

num = [26,89,5,775,0,-1]
if num[0] > num[1]:
    b = num[0]
    second_large = num[1]
else:
    second_large = num[0]
    b = num[1]
for i in range(2,len(num)):
    if num[i] > b:
        second_large = b
        b = num[i]
    elif num[i] > second_large:
        second_large = num[i]

print(second_large) 
