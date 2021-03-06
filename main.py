import os
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("WorkSans-Bold.ttf", 64)

name = input("First Name: \n")
middlename = input("Middle Name: \n")
lastname = input("Last Name: \n")

img = Image.open('cert-template.jpg')
draw = ImageDraw.Draw(img)
name_middle = False
middle_last = False
last_middle = False

name , lastname , middlename = name.title() , lastname.title() , middlename.title()

if middlename != '':
	if len(name + middlename + lastname) <= 13:
		draw.text((340,325), name + " "+ middlename + " "+ lastname, (255,0,0), font)
	elif len(name + middlename + lastname) > 13:
		if len(name + middlename) <= 13:
			draw.text((340,325), name + " " + middlename, (255,0,0), font)
			draw.text((340,400), lastname, (255,0,0), font)
			name_middle = True
	else:
		draw.text((340,325),name, (255,0,0), font)

	if name_middle == False and len(middlename + lastname) <= 13:
		draw.text((340,400),middlename + " " + lastname, (255,0,0), font)
		last_middle = True
	elif last_middle==False and name_middle==False:
		middlename = middlename[0].upper()
		draw.text((340,400),middlename + " " + lastname, (255,0,0), font)
else:
	draw.text((340,325), name + " "+ lastname, (255,0,0), font)
	

rgb_im = img.convert('RGB')
rgb_im.save(f'certs/{name+"_"+middlename+"_"+lastname}.jpg'.replace(" ", "").lower())
