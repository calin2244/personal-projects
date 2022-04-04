import urllib
from urllib import request
from PIL import Image

#Am descarcat poza in folder
#url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
#r = request.urlopen(url)
#with open("color.jpg", "wb") as file:
    #file.write(r.read())
    
try:
    img = Image.open("color.jpg")
except:
    pass

pixel_values = list(img.getdata())
nw = ""

end = 609
step = 7
y = 46

for x in range(0,end,step):
    coordinate = x, y
    nw += chr(img.getpixel(coordinate)[0])
lst = [105, 110, 116, 101, 103, 114, 105, 116, 121]
new_lst = [chr(x) for x in lst]
print(''.join(new_lst))
