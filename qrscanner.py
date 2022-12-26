import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


# create or make
a = pyqrcode.create("https://www.simplilearn.com/")
a.png("my.png", scale = 8)

b = decode(Image.open("my.png"))
print(b[0].data.decode("ascii"))