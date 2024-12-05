import pytesseract
from PIL import Image

def extract_text_from_image(image_path, languages="eng+hin"):
    """
    Extract text from an image using Tesseract OCR.

    Parameters:
        image_path (str): Path to the image file.
        languages (str): The language(s) to be used by Tesseract. Default is English.
        
    Returns:
        str: Extracted text from the image.
    """
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Use Tesseract to extract text
        extracted_text = pytesseract.image_to_string(img, lang=languages)
        return extracted_text
    except Exception as e:
        return f"Error in OCR processing: {e}"