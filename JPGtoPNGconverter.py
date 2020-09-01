import sys, os
import re
from PIL import Image

# grab the first and second argument
# first - folder's name with jpg image
# second - folder's name with png image
first_folder = sys.argv[1]
second_folder = sys.argv[2]

valid_pattern = re.compile(r"[a-zA-Z0-9-]{1,}\/$")

try:
	# checking is folder's name is valid
	is_first_folder = valid_pattern.fullmatch(first_folder)
	is_second_folder = valid_pattern.fullmatch(second_folder)

	if not is_first_folder or not is_second_folder:
  		raise Exception("Wrong name of folder")

	# if second not exists - to create
	if not os.access("./" + second_folder, os.F_OK):
		os.mkdir("./" + second_folder)

	# get list of pics from first folder	
	name_pics_list = os.listdir("./" + first_folder)

	# function to convert image
	def convert_to_png(first_folder, second_folder, name_file):
		img = Image.open("./" + first_folder + name_file)
		name_file_without_jpg = name_file.split('.')
		name = ""
		for i in range(len(name_file_without_jpg) - 1):
			name += name_file_without_jpg[i] + "."
		img.save("./" + second_folder + name + "png", "png")

	# loop through first folder and convert
	for name_pic in name_pics_list:
		convert_to_png(first_folder, second_folder, name_pic)
except Exception as err:
	print(err)









