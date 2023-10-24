from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Guvi:
   def __init__(self):
       self.url = "https://www.saucedemo.com/"
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

   def webpage_details(self):
       self.driver.maximize_window()
       self.driver.get(self.url)
       print(self.driver.title)
       print(self.driver.current_url)
       print("Please find the extracted contents of  the webpage saucedemo in the text file Webpage_task_19.txt.")


   def print_page_text_file(self):
       try:
           f = open("Webpage_task_19.txt", "w")
           sleep(4)
           text = (self.driver.find_element(By.XPATH, "/html/body").text)
           f.write(text)
           sleep(4)
           f.close()
       except NoSuchElementException as selenium_error:
           print(selenium_error)
       finally:
           self.driver.close()



webpage = Guvi()
webpage.webpage_details()
webpage.print_page_text_file()
