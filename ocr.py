from PIL import Image
import pytesseract

# Load the image
image = Image.open("image.png")

# Extract text
text = pytesseract.image_to_string(image)

print(text)
