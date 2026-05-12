# Overlaying shirt.png(Transparent background) on Iyyappa.png(user photo) after resizing and cropping the input to same size saving result as output

import sys
from PIL import Image, ImageOps

valid = (".jpg", ".jpeg", ".png")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].lower().endswith(valid) or not sys.argv[2].lower().endswith(valid):
    sys.exit("Not a valid file")
elif sys.argv[1].lower().split(".")[-1] != sys.argv[2].lower().split(".")[-1]:
    sys.exit("Input and Output have different exensions")
else:
    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        image = ImageOps.fit(image,shirt.size)
        image.paste(shirt,(0, 0), shirt)
        image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")
