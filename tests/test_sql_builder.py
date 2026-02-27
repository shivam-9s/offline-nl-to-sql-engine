import unittest
from parser.ast import QueryNode
from builder.sql_builder import build_sql

class TestSQLBuilder(unittest.TestCase):

    def test_select_query(self):
        query = QueryNode(
            "SELECT",
            table="employees",
            conditions=[{
                "column": "salary",
                "operator": ">",
                "value": "50000",
                "logical": None
            }]
        )

        sql = build_sql(query)

        self.assertEqual(
            sql,
            "SELECT * FROM employees WHERE salary > 50000;"
        )

if __name__ == "__main__":
    unittest.main()
