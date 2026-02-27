import unittest
from parser.ast import QueryNode
from mapper.schema_mapper import validate_query

class TestMapper(unittest.TestCase):

    def test_valid_column(self):
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

        validated = validate_query(query)
        self.assertEqual(validated.table, "employees")

if __name__ == "__main__":
    unittest.main()
