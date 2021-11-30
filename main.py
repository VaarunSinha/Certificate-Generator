import os
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("WorkSans-Bold.ttf", 64)

name = input("First Name: \n")
lastname = input("Last Name: \n")
middlename = input("Middle Name: \n")
# middlename = middlename[0].upper()

img = Image.open('cert-template.jpg')
draw = ImageDraw.Draw(img)
name_middle = False

if len(name + middlename + lastname) <= 13:
    draw.text((340,325), name + " "+ middlename + " "+ lastname, (255,0,0), font)
elif len(name + middlename + lastname) > 13:
    if len(name + middlename) <= 13:
        draw.text((340,325), name + " " + middlename, (255,0,0), font)
        draw.text((340,400),lastname, (255,0,0), font)
        name_middle = True
    else:
        draw.text((340,325),name, (255,0,0), font)

    if name_middle == False and len(lastname + middlename) > 13:
        middlename = middlename[0].upper()
        draw.text((340, 400), middlename + " " + lastname, (255,0,0), font)
    elif len(lastname + middlename) <= 13:
        draw.text((340, 400), middlename + " " + lastname, (255,0,0), font)

rgb_im = img.convert('RGB')
rgb_im.save(f'certs/{name}.jpg')