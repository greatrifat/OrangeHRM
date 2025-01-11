import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "https://opensource-demo.orangehrmlive.com"
       
    
    @classmethod
    def tearDownClass(cls):
        # Quit the WebDriver after all tests
        cls.driver.quit()

    def test_valid_login(self):
        """Test valid login credentials."""

        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

        # Verify successful login by checking if the Dashboard heading is displayed
        dashboard = self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        dashboard_text = dashboard.text
        self.assertEqual(dashboard_text, "Dashboard", "Login failed or Dashboard not displayed.")

   
    

if __name__ == "__main__":
    unittest.main()