# mapper/schema_mapper.py

from config.schema import SCHEMA

def validate_query(query_node):

    if query_node.table not in SCHEMA:
        raise Exception("Invalid table")

    for condition in query_node.conditions:
        column = condition["column"]
        if column not in SCHEMA[query_node.table]["columns"]:
            raise Exception(f"Invalid column: {column}")

    return query_node
