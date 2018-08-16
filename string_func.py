#Python code to swap cases
text = str("Veryx technologies")
for i in range (len(text)):
    if text[i].isupper():
        print (text[i].lower(),)
    elif text[i].islower():
        print (text[i].upper()),
