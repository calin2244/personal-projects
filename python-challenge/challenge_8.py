import bz2
from urllib import request
import requests
import re

with open("regex.txt", "r") as file:
    file.seek(0)
    content = file.read()

url = request.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').readlines()[20:22]
data1 = ''.join(url[0].decode('utf-8'))
data2 = ''.join(url[1].decode('utf-8'))
out = re.search("'(.*)", data1).group()
out2 = re.search("'.*", data2).group()
out = eval("b%s" %out)
out2 = eval("b%s" %out2)
print("The username is ", bz2.decompress(out))
print("The password is ", bz2.decompress(out2))
