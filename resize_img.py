"""Resize image to xxhdpi xhdpi hdpi mdpi.

The origin image is designed in ndp * 18 px size. For example:
an icon(48dp * 48dp) will be designed in 864px * 864px.
With these images, the script will generate images in xxhdpi
xhdpi hdpi and mdpi.

"""

from PIL import Image
import os

size_info = {'xxhdpi': 6, 'xhdpi': 9, 'hdpi': 12, 
	'mdpi': 18}

# Get images and remove script
images = os.listdir('.')
images.remove('resize_img.py')

# Create directories
for dir_name in size_info.keys():
	os.mkdir(dir_name)

# Resize image and store into correct directory
for image in images:
	img = Image.open(image)
	origin_size = img.size

	for key, value in size_info.items():
		target_size = (origin_size[0]/value, origin_size[1]/value)
		new_img = img.resize(target_size)
		new_img.save(os.path.join(key, image))
