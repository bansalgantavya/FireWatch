
from PIL import Image
image_path=r"C:\Users\deepak\Desktop\Dhruv\codes\image analysis\red.png"
image= Image.open(image_path)


# image.show()  # to show an image
# width,height= image.size  # to get size of image
# mode=image.mode # to represent color mode of image
# pixel_value=image.getpixel((x,y))  # pixel access
# pixel_format=image.format #returns format of image
# exif_data=image.info.get("exif")  # returns exif data only for jpg format
# histogram=image.histogram  # image histogram
# image_info=image.info # image attributes and description

# print(image_info)



# Image resizing and rescaling
new_size=(40000,30000)
resized_image=image.resize(new_size)
resized_image.show()