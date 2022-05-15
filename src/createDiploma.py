from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

urlImage = "https://certificates.zdynamics.org/assets/Diploma.png"

print(urlImage)

img = Image.open(urlImage)
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype("sans-serif.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
# draw.text((0, 0),"Sample Text",(255,255,255))
# img.save('z.png')
