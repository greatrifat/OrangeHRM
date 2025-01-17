import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class AddSystemUserTest(unittest.TestCase):
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
    
    def test_add_new_employee(self):
        """Verify adding a new Employee."""
        self.driver.get(self.base_url)

        # Log in as Admin
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()    
        # Wait for the dashboard to load
        admin_menu = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        admin_menu.click()
        # Click Add  
        add_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
        add_button.click()

        firstName_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='firstName']")))
        firstName_input.send_keys("Md Robayet")
        middleName_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='middleName']")))
        middleName_input.send_keys("Ahasan")
        lastName_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='lastName']")))
        lastName_input.send_keys("Rifat")

        employeeId_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-v-957b4417]//input[@class='oxd-input oxd-input--active']")))
        employeeId_input.clear()
        time.sleep(5)
        employeeId_input.send_keys("5678")

        logIn_checkbox = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'oxd-switch-input')]")))
        logIn_checkbox.click()

        
        userName_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Username']//following::input[1]")))
        userName_input.send_keys("greatrifat")

        password_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Password']//following::input[1]")))
        password_input.send_keys("Greatrifat@2")

        cpassword_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Confirm Password']//following::input[1]")))
        cpassword_input.send_keys("Greatrifat@2")

        #employee image add
        upload_button = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'employee-image-action') and @type='button']")))
        upload_button.click()
        file_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file' and contains(@class, 'oxd-file-input')]")))
        file_input.send_keys("E:/Rifat/Project/SQA/OrangeHRM-Selenium-Python/employee.jpeg")

        save_btn = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        save_btn.click()
        time.sleep(5)


    
    def test_delete_employee(self):
        """Verify deleting a Employee."""
        # self.driver.get(self.base_url)

        # # Log in as Admin
        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()    
        # Wait for the dashboard to load
        admin_menu = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        admin_menu.click()
        
        employeeId_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Employee Id']//following::input[1]")))
        employeeId_input.send_keys("03985678")
        
        # Click Searech  
        search_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']")))
        search_button.click()

        delete_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'bi-trash')]/ancestor::button")))
        delete_button.click()

        confirm_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes, Delete']")))
        confirm_button.click()

        time.sleep(5)

        

        

        

        

        




        
        
if __name__ == "__main__":
    unittest.main()
