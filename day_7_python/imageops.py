# image operations with pillow liberary PIL Python Image Liberary
from PIL import Image

# Read the image
photo  = Image.open('img.jpg')

# print the type of image
print(type(photo))

# To See the image
#photo.show()

# To Check the Size 
print(photo.size)

# Crope the image
# left top right bottom 
cropped = photo.crop((1024, 1024, 3072, 3072))
cropped.show()


# Rotate the image
rotated = photo.rotate(90)
#rotated.show()

# To save the image
rotated.save('rotated.jpg')