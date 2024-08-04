import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

#PS path will vary for you 
image_path = '/Users/calvin/Desktop/CAPTCHA/dataset'
image_extension = {'.png', '.jpg'}

for imagename in os.listdir(image_path):
    if any(imagename.endswith(ext) for ext in image_extension):
        filepath = os.path.join(image_path, imagename)

        with Image.open(filepath) as img:
            text = pytesseract.image_to_string(img)

            if text.strip():
                print(f"Extraction from {imagename}: {text}")


