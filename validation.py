import re

def validate_data(id_type, extracted_text):
    """
    Validate the extracted data based on document type (e.g., Aadhaar, PAN).

    Parameters:
        id_type (str): The type of identity document (e.g., Aadhaar, PAN).
        extracted_text (str): Extracted text from the document.
        
    Returns:
        bool: Whether the extracted text is valid based on the document type.
    """
    try:
        if id_type == "Aadhaar":
            # Aadhaar validation logic (12 digits, grouped in 4s)
            if re.search(r'\d{4}\s?\d{4}\s?\d{4}', extracted_text):
                return True
        elif id_type == "PAN Card":
            # PAN Card validation logic (ABCDE1234F)
            if re.search(r'[A-Z]{5}\d{4}[A-Z]', extracted_text):
                return True
        elif id_type == "Voter ID":
            # Basic voter ID validation (can be extended)
            if "Voter ID" in extracted_text or re.search(r'[A-Z]{3}\d{7}', extracted_text):
                return True
        else:
            # Validation for other types of documents can be added here
            return False

        return False
    except Exception as e:
        return False