def lm(c):
    if ord(c) >=65 and ord(c)<=90:
        return True
    else:
        return False

lst = []

with open("regex.txt", "r") as myfile:
    #myfile.seek(0)
    lst = myfile.read()
 
nw = ""  
for i in range(3,len(lst)-3):
    if ord(lst[i])>=97 and ord(lst[i]) <=122:
        if lm(lst[i+1]) and lm(lst[i+2]) and lm(lst[i+3]) and lm(lst[i-1]) and lm(lst[i-2]) and lm(lst[i-3]):
            if lm(lst[i-4]) == False and lm(lst[i+4]) == False:
                nw+=lst[i]
print(nw)
