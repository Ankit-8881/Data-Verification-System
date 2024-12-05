import spacy
import re
from fuzzywuzzy import fuzz

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def extract_entities_from_text(text):
    """
    Extracts names and DOB from text with fallback patterns.
    """
    doc = nlp(text)
    entities = {"PERSON": [], "DATE": []}

    # Extract names using NLP (PERSON)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["PERSON"].append(ent.text.strip())
    
    # Custom Regex for Father's Name and Mother's Name
    custom_patterns = [
        (r"(Father['s]* Name|Father):?\s*([^\n]+)", "PERSON"),
        (r"(Mother['s]* Name|Mother):?\s*([^\n]+)", "PERSON"),
    ]
    for pattern, entity_type in custom_patterns:
        matches = re.findall(pattern, text)
        for _, value in matches:
            entities[entity_type].append(value.strip())

    # Custom DOB extraction
    dob_patterns = [
        r"(DOB|Date of Birth|जन्‍म लियि)[\s:]*([\d]{2}/[\d]{2}/[\d]{4})",
        r"[\d]{2}/[\d]{2}/[\d]{4}",  # Handle loose DOB patterns
    ]

    for pattern in dob_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if isinstance(match, tuple):
                entities["DATE"].append(match[1])
            else:
                entities["DATE"].append(match)

    return entities

def normalize_date(date_str):
    """
    Normalize DOB from various formats (DD/MM/YYYY or YYYY-MM-DD) to uniform DD-MM-YYYY.
    """
    try:
        parts = re.split(r"[-/]", date_str)
        if len(parts) == 3:
            day, month, year = parts if len(parts[0]) == 2 else parts[::-1]
            return f"{day.zfill(2)}-{month.zfill(2)}-{year}"
    except ValueError:
        return date_str  # Fallback without crash
    return date_str

def preprocess_candidate(candidate):
    """
    Preprocess the candidate name to remove unwanted characters and format it.
    """
    candidate = candidate.strip().lower()  # Normalize case and strip whitespace
    candidate = re.sub(r'[^a-zA-Z\s]', '', candidate)  # Remove non-alphabetic characters
    return candidate

def match_entities_across_documents(entity_type, target_value, extracted_texts, threshold=75):
    """
    Fuzzy match for specific field (Name, DOB).
    """
    match_count = 0
    target_value = normalize_date(target_value) if entity_type == "DOB" else target_value

    for text in extracted_texts:
        entities = extract_entities_from_text(text)
        candidates = entities.get("PERSON" if entity_type in ["Name", "Father's Name", "Mother's Name"] else "DATE", [])

        for candidate in candidates:
            candidate = normalize_date(candidate) if entity_type == "DOB" else preprocess_candidate(candidate)

            # Debugging: Log the comparison
            similarity_score = fuzz.ratio(target_value.lower(), candidate.lower())
            if similarity_score < threshold:
                print(f"Mismatch: '{target_value}' (target) vs '{candidate}' (candidate) - Similarity: {similarity_score}")

            if similarity_score >= threshold:
                match_count += 1
                break

    return match_count