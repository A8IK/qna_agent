import unittest
from src.pre_process import preprocess
from src.ques_parsing import parse_question
from src.ans_generating import find_answer

class TestQnASystem(unittest.TestCase):

    def test_preprocess(self):
        raw_text = "Bangladesh[1] is a country in South Asia."
        expected = "Bangladesh is a country in South Asia."
        self.assertEqual(preprocess(raw_text), expected)

    def test_parse_question(self):
        question = "What is the capital of Bangladesh?"
        expected_keywords = ["What", "is", "the", "capital", "of", "Bangladesh"]
        self.assertEqual(parse_question(question), expected_keywords)

    def test_find_answer(self):
        content = "Dhaka is the capital of Bangladesh. It is known for its rich culture."
        keywords = ["capital", "Bangladesh"]
        expected = "Dhaka is the capital of Bangladesh"
        self.assertEqual(find_answer(keywords, content), expected)

if __name__ == "__main__":
    unittest.main()
