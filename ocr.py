import pytesseract
from pdf2image import convert_from_path

pdf_path = "/Users/gman/Downloads/1293857.pdf"

# Convert PDF pages to images
images = convert_from_path(pdf_path)

# Run OCR on each image
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image)
    print(f"Page {i + 1}:\n{text}\n")