from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class Guvi:
   def __init__(self):
       self.url = "https://www.saucedemo.com/"
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


   def login(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           sleep(4)
           self.driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")
           sleep(4)
           self.driver.find_element(by=By.ID, value="password").send_keys("secret_sauce")
           sleep(4)
           self.driver.find_element(by=By.ID, value="login-button").click()
           sleep(4)
       except NoSuchElementException as selenium_error:
           print(selenium_error)
       finally:
           self.driver.close()


swag = Guvi()
swag.login()

