import unittest

from translator import englishToFrench,frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertEqual(englishtofrench("welcome"),"Bienvenue")
        self.assertEqual(englishtofrench("love"),"Amour")
        self.assertIsNotNone(englishText)

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertEqual(frenchToEnglish("Bienvenue"),"welcome")
        self.assertEqual(frenchToEnglish("Amour"),"love")
        self.assertIsNotNone(frenchText)

unittest.main()
