

from PIL import Image

my_image = Image.open("pup.jpg")
image_pixels = my_image.load()
width, height  = my_image.size
for i in range(0, width):
    for j in range(0, height):
        current_pixel = image_pixels[i,j]
        blue_component = image_pixels[i,j][0]
        green_component = image_pixels[i,j][1]
        red_component = image_pixels[i,j][2]
        gray_value = (int)(0.07 * blue_component + 0.72 * green_component + 0.21 * red_component)
        image_pixels[i,j] = (gray_value, gray_value, gray_value, 255)


my_image.show()
