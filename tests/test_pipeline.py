import unittest
from main import process_query

class TestPipeline(unittest.TestCase):

    def test_and_condition(self):
        result = process_query(
            "show employees salary > 50000 and age < 40"
        )

        self.assertEqual(
            result,
            "SELECT * FROM employees WHERE salary > 50000 AND age < 40;"
        )


if __name__ == "__main__":
    unittest.main()
