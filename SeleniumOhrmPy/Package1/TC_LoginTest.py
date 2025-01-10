import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("This is login by email test")
        self.assertTrue(True)
    
    def test_loginbyFb(self):
        print("This is login by fb test")
        self.assertTrue(True)

    def test_loginbyX(self):
        print("This is login by X test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()