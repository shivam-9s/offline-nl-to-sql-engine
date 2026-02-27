import unittest
from preprocessing.normalizer import normalize_text

class TestNormalizer(unittest.TestCase):

    def test_synonym_replacement(self):
        text = "Show workers earning more than 50000"
        result = normalize_text(text)
        self.assertEqual(result, "show employees salary > 50000")

if __name__ == "__main__":
    unittest.main()
