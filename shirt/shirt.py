import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) == 3:
    input_ext = os.path.splitext(sys.argv[1])[1].lower()
    output_ext = os.path.splitext(sys.argv[2])[1].lower()
    valid_ext = ['.jpg','.jpeg','.png']
    if input_ext in valid_ext and output_ext in valid_ext:
        if input_ext == output_ext:
            try:
                user_img = Image.open(sys.argv[1])
                shirt = Image.open('shirt.png')
                size = shirt.size
                user_img = ImageOps.fit(user_img, size, bleed=0.0, centering=(0.5, 0.5))
                user_img.paste(shirt, shirt)

                user_img.save(sys.argv[2])
            except FileNotFoundError:
                sys.exit('Input does not exist')
        else:
            sys.exit('Input and output have different extensions')
    else:
        sys.exit('Invalid input or output')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')