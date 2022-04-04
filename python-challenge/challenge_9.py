import urllib
from urllib import request

with open('first.text', 'r') as file:
    file.seek(0)
    content = file.read()
    
with open('second.txt', 'r') as file:
    content2 = file.read()

content = content.replace(',',' ')
content2 = content2.replace(',',' ')

nw = ""
nw2 = ""
i = 0
j = 0
lst1 = []
lst2 = []
lst3 = []
for char in content:
    if char != ' ':
        nw += char
    elif char == ' ' or char == NULL:
        lst1.append(int(nw))
        nw = ""
        i +=1
for char2 in content2:
    if char2 != ' ':
        nw2 += char2
    elif char2 == ' ' or char2 == NULL:
        lst2.append(int(nw2))
        nw2 = ""
        j +=1 
lst1.append(int(nw))
lst2.append(int(nw2))

for i in range(min(len(lst1),len(lst2))):
    lst3.append(lst1[i]+lst2[i])
for i in range(112,len(lst1)):
    lst3.append(lst1[i])

nw4 = ""
nr = 0
for i in range(len(lst3)):
    if lst3[i]>=65 and lst3[i]<=90:
        nw4 += chr(lst3[i])
    elif lst3[i]>=97 and lst3[i]<=122:
        nw4 += chr(lst3[i])
    if lst3[i] == 524:
        nr+=1
print(nr)

