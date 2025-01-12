from HtmlTestRunner import HTMLTestRunner
import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest
from Package2.TC_Payment import PaymentTest
from Package2.TC_Method import MethodTest

TC1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
TC2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
TC3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
TC4 = unittest.TestLoader().loadTestsFromTestCase(MethodTest)

sanityTestSuit = unittest.TestSuite([TC1,TC2])
functionalTestSuit = unittest.TestSuite([TC3,TC4])
masterTestSuit = unittest.TestSuite([TC1,TC2,TC3,TC4])
currentSuite = unittest.TestSuite([TC1])
#unittest.TextTestRunner(verbosity=2).run(masterTestSuit)

# Configure HTMLTestRunner
runner = HTMLTestRunner(output='Test_Results_HC')

runner.run(currentSuite)
print("Report generated in the 'Test_Results' directory.")