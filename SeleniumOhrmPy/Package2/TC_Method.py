import unittest

class MethodTest(unittest.TestCase):
    def test_methodbyBank(self):
        print("This is method by bank test")
        self.assertTrue(True)
    
    def test_methodbyCash(self):
        print("This is method by cash test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()