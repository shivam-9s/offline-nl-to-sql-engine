# builder/sql_builder.py

def build_sql(query_node):

    # Base query depending on action
    if query_node.action == "SELECT":
        sql = f"SELECT * FROM {query_node.table}"
    elif query_node.action == "COUNT":
        sql = f"SELECT COUNT(*) FROM {query_node.table}"
    else:
        sql = f"SELECT * FROM {query_node.table}"

    # Add conditions if present
    if query_node.conditions:
        condition_strings = []

        for i, cond in enumerate(query_node.conditions):
            part = f"{cond['column']} {cond['operator']} {cond['value']}"

            if i == 0:
                condition_strings.append(part)
            else:
                condition_strings.append(f"{cond['logical']} {part}")

        sql += " WHERE " + " ".join(condition_strings)

    sql += ";"
    return sql
