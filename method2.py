from PIL import Image
import numpy as np

def main():
     image_array = np.array(Image.open("hannibal.jpg"))

     for i in range(len(image_array)):
          for j in range(len(image_array[i])):
               blue = image_array[i, j, 0]
               green = image_array[i, j, 1]
               red = image_array[i, j, 2]
               gray = (red + green + blue) / 3
               image_array [i,j] = gray

     return(image_array)

image_array = main()
save_image = Image.fromarray(image_array)
save_image.save('method-divisions-hannibal.jpg')