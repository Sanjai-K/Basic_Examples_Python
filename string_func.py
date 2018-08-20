#Python code to swap cases
text = raw_input("Enter a string : ")
for i in range (len(text)):
    if text[i].isupper():
        print (text[i].lower()),
    elif text[i].islower():
        print (text[i].upper()),
