
# intent/classifier.py

def classify_intent(text: str) -> str:
    if "count" in text:
        return "COUNT"
    if "sum" in text or "total" in text:
        return "SUM"
    if "average" in text:
        return "AVG"
    if "delete" in text:
        return "DELETE"
    if "update" in text:
        return "UPDATE"
    
    return "SELECT"
