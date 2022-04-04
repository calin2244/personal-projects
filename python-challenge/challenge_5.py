import urllib
import pickle
from urllib import request

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
resp = request.urlopen(url)
data = pickle.load(resp)
for x in data:
    print(''.join([key * val for key,val in x]))