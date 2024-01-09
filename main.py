from PIL import Image

with Image.open("hannibal.jpg") as im:
    px = im.load()
print(px[4, 4])
px[4, 4] = (0, 0, 0)
print(px[4, 4])