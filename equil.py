#python program to print equilateral triangle

'''a = input ("num:")
for i in range (0,a):
    for j in range (0,a-1):
        print (" ")
    for j in range (0,i):
        print ("*")'''



row=input("enter the rows: ")
for i in range(0,row):
    print ((row-i)*' '+((i)*'*')+((i+1)*'*'))
