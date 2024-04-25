import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Path to the image file
image_path = r"C:\Users\dwith\OneDrive\Documents\Tesseract_txt extraction\text3.png.jpg"

# Read text from the image
results = reader.readtext(image_path)

# Print the extracted text
for (bbox, text, prob) in results:
    print(f"Text: {text}")