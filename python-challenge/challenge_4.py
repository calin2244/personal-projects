import requests
import re
from re import compile
import urllib
from urllib import request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
resp = request.urlopen(url)
html = resp.read().decode("utf-8")

link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
response = requests.get(link + '63579')



while True:
    response.raise_for_status
    nextNothingRegex = re.compile(r'\d+')
    matchObj = re.search(nextNothingRegex, response.text)
    matchObj2 = re.findall(nextNothingRegex, response.text)
    nextNothing = matchObj[0]
    print(nextNothing)
    response = requests.get(link + nextNothing)

print(matchObj2)