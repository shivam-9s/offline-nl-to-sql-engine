import unittest
from parser.grammar import parse_query

class TestParser(unittest.TestCase):

    def test_basic_condition(self):
        text = "show employees salary > 50000"
        intent = "SELECT"
        result = parse_query(text, intent)

        self.assertEqual(result.table, "employees")

        self.assertEqual(
            result.conditions[0],
            {
                "column": "salary",
                "operator": ">",
                "value": "50000",
                "logical": None
            }
        )

if __name__ == "__main__":
    unittest.main()
