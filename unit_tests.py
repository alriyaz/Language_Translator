import unittest
from translator import englishtofrench
from translator import englishtogerman

class TestEF(unittest.TestCase):
    def test1(self): 
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
    def test2(self):
        self.assertEqual(englishtofrench("How are you"), "Comment vous êtes")
    def test3(self): 
        self.assertEqual(englishtofrench("Stay healthy and happy"), "Restez en santé et heureux")
    def test4(self): 
        self.assertEqual(englishtofrench(""), "No input provided")

class TestEG(unittest.TestCase):
    def test_1(self): 
        self.assertEqual(englishtogerman("Hello"), "Hallo")
    def test_2(self): 
        self.assertEqual(englishtogerman("How are you"), "Wie geht es Ihnen?")
    def test_3(self): 
        self.assertEqual(englishtogerman("Stay healthy and happy"), "Gesund und glücklich bleiben")
    def test4(self): 
        self.assertEqual(englishtogerman(""), "No input provided")

unittest.main()
