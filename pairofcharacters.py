import string
from PIL import Image, ImageDraw
lower = string.ascii_lowercase
upper = string.ascii_uppercase
for i in lower:
    for j in lower:
        img = Image.new('RGB', (100, 30), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((10,10), '{}'.format(i), fill=(0,0,0))
        d.text((14,10), '{}'.format(j), fill=(0,0,0))
        img.save('{}{}.png'.format(i,j))

 
