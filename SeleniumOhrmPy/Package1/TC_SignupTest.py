import unittest

class SignupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("This is signup by email test")
        self.assertTrue(True)
    
    def test_signupbyFb(self):
        print("This is signup by fb test")
        self.assertTrue(True)
        
    @unittest.skip("This is a skipped test.")
    def test_signupbyX(self):
        print("This is signup by X test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()