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
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        # Quit the WebDriver after all tests
        cls.driver.quit()

    def login(self, username, password):
        """
        Helper method to perform login.
        :param username: Username for login
        :param password: Password for login
        """
        self.driver.get(self.base_url)
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def is_dashboard_displayed(self):
        """
        Helper method to check if the Dashboard is displayed.
        :return: True if Dashboard is displayed, False otherwise
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
            )
            return True
        except:
            return False

    def test_valid_username_pass(self):
        """Test valid login credentials."""
        self.login("Admin", "admin123")
        self.assertTrue(self.is_dashboard_displayed(), "Dashboard not displayed after valid login.")

    def test_valid_username_invalid_pass(self):
        """Test invalid login credentials."""
        self.login("Admin", "wrongpass")
        error_message = self.driver.find_element(By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]").text
        self.assertEqual(error_message, "Invalid credentials", "Invalid credentials error message not displayed.")

    def test_invalid_username_valid_pass(self):
        """Test invalid login credentials."""
        self.login("wronguser", "admin123")
        error_message = self.driver.find_element(By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]").text
        self.assertEqual(error_message, "Invalid credentials", "Invalid credentials error message not displayed.")

    def test_invalid_username_invalid_pass(self):
        """Test invalid login credentials."""
        self.login("wronguser", "wrongpass")
        error_message = self.driver.find_element(By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]").text
        self.assertEqual(error_message, "Invalid credentials", "Invalid credentials error message not displayed.")

if __name__ == "__main__":
    unittest.main()