from PIL import Image
import cv2
import numpy as np

def preprocess_image(image_path, processed_dir):
    """
    Preprocess the uploaded image (resize, convert to grayscale, etc.)

    Parameters:
        image_path (str): Path to the uploaded image.
        processed_dir (str): Directory where the processed image will be saved.
        
    Returns:
        str: Path to the preprocessed image.
    """
    try:
        # Load the image
        img = Image.open(image_path)
        
        
        img = img.resize((800, 800))
        
        # Convert image to grayscale for better OCR accuracy
        img_gray = img.convert('L')
        
        # Save preprocessed image
        processed_path = f"{processed_dir}/{image_path.split('/')[-1]}"
        img_gray.save(processed_path)
        
        return processed_path
    except Exception as e:
        return f"Error in image preprocessing: {e}"