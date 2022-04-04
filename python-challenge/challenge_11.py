from urllib import request
from PIL import Image

img = Image.open("cave.jpg")
pixel_vals = list(img.getdata())
size = width, height = img.size
new_img = Image.new('RGB', size)

for x in range(0, width, 2):
    for y in range(0, height, 2):
        even_color = img.getpixel((x,y))[0]
        odd_color = img.getpixel((x+1,y+1))[1]
        
        new_img.putpixel((x,y), even_color)
        new_img.putpixel((x,y), odd_color)
        
new_img.save("odd_even.png")