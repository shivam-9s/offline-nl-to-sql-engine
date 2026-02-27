# preprocessing/normalizer.py

import re
from config.synonyms import SYNONYMS

def normalize_text(text: str) -> str:
    text = text.lower()

    # Replace multi-word synonyms first
    for key in sorted(SYNONYMS.keys(), key=len, reverse=True):
        text = text.replace(key, SYNONYMS[key])

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text
