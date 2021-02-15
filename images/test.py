from PIL import Image
import numpy as np 


im = open("test.png", 'rb')
# array = np.array(im)
im.close()
im = Image.open("test.png")
print(im)