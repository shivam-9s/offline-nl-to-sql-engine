import unittest
from intent.classifier import classify_intent

class TestIntent(unittest.TestCase):

    def test_select_default(self):
        self.assertEqual(classify_intent("show employees"), "SELECT")

    def test_count(self):
        self.assertEqual(classify_intent("count employees"), "COUNT")

if __name__ == "__main__":
    unittest.main()
