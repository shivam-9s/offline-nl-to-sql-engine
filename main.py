from preprocessing.normalizer import normalize_text
from intent.classifier import classify_intent
from parser.grammar import parse_query
from mapper.schema_mapper import validate_query
from builder.sql_builder import build_sql

def process_query(user_input):

    text = normalize_text(user_input)
    intent = classify_intent(text)
    parsed = parse_query(text, intent)
    validated = validate_query(parsed)
    sql = build_sql(validated)

    return sql


if __name__ == "__main__":
    user_input = input("Enter query: ")
    print(process_query(user_input))
