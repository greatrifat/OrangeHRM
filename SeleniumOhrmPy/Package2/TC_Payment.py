import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentbyDollar(self):
        print("This is payment by dollar test")
        self.assertTrue(True)
    
    def test_paymentbyTaka(self):
        print("This is payment by taka test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()