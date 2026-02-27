import re
from parser.ast import QueryNode

def parse_query(text: str, intent: str) -> QueryNode:
    tokens = text.split()

    # Detect table
    table = None
    for token in tokens:
        if token in ["employees", "departments"]:
            table = token
            break

    # Extract all conditions
    pattern = r'(\w+)\s*(>|<|=)\s*(\d+)'
    matches = list(re.finditer(pattern, text))

    conditions = []

    for i, match in enumerate(matches):
        column, operator, value = match.groups()

        logical = None
        if i > 0:
            # Check text between previous and current match
            prev_end = matches[i - 1].end()
            current_start = match.start()
            between_text = text[prev_end:current_start]

            if "and" in between_text:
                logical = "AND"
            elif "or" in between_text:
                logical = "OR"

        conditions.append({
            "column": column,
            "operator": operator,
            "value": value,
            "logical": logical
        })

    return QueryNode(action=intent, table=table, conditions=conditions)
