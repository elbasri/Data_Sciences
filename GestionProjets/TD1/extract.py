import pytesseract as pyt
img_path = '/mnt/data/Screenshot from 2024-02-13 11-40-37.png'

img = Image.open(img_path)



# Use tesseract to do OCR on the image without specifying the language

text = pyt.image_to_string(img)


