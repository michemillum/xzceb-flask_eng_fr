import unittest
from translator import englishToFrench
from translator import frenchToEnglish
class TestMyModule1(unittest.TestCase):
    def test_e2f1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    def test_e2f2(self):
        self.assertEqual(englishToFrench('Green'), 'Vert')
    def test_e2f3(self):
        self.assertNotEqual(englishToFrench('None'),'')
    def test_e2f4(self):
        self.assertNotEqual(englishToFrench(0),0)

class TestMyModule2(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    def test_f2e2(self):
        self.assertEqual(frenchToEnglish('Vert'), 'Green')
    def test_f2e3(self):
        self.assertNotEqual(frenchToEnglish('None'),'')
    def test_f2e4(self):
        self.assertNotEqual(frenchToEnglish(0),0)

unittest.main()