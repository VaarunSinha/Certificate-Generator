import os
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("WorkSans-Bold.ttf", 60)

name = input("Name of participant: \n")

img = Image.open('cert-template.jpg')
draw = ImageDraw.Draw(img)
draw.text((340,325), name, (255,0,0), font)
rgb_im = img.convert('RGB')
rgb_im.save(f'certs/{name}.jpg')