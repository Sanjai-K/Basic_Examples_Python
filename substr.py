#Python code to find the substring in an input string

import re
a=raw_input("enter the string : ")
b=raw_input("String to be found : ")
c=re.findall(b,a)
print(len(c)) 
