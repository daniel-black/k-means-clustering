from image_utils import *
from k_means import *

# inputs for the image and k
file = input("Enter image file > ")
k = int(input('Enter how many colors > '))

print('...processing...')
image = read_ppm(file)

# k means algorithm used to produce new image
newImage = k_means(image, k)
print('New modified image generated')

# new image saved to file "newImage.ppm"
save_ppm("newImage.ppm", newImage)
print('New modified image saved')

