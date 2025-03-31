import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command line arguments")

input_path = sys.argv[1]
output_path = sys.argv[2]
extensions = [".jpg", ".jpeg", ".png"]

input_ext = os.path.splitext(input_path)[1].lower()
output_ext = os.path.splitext(output_path)[1].lower()

if input_ext not in extensions or output_ext not in extensions:
    sys.exit("Invalid input")

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

try:
    input_img = Image.open(input_path)
    shirt = Image.open("shirt.png")

except FileNotFoundError:
    sys.exit("File does not exist")

else:
    input_img = ImageOps.fit(input_img, size=shirt.size)
    input_img.paste(shirt, shirt)
    input_img.save(output_path)
