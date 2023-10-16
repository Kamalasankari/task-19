from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class Guvi:
   def __init__(self):
       self.url = "https://www.guvi.in/"
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

   def webpage_details(self):
       self.driver.maximize_window()
       self.driver.get(self.url)
       print(self.driver.title)
       print(self.driver.current_url)


   def print_page_text_file(self):
       f = open("Webpage_task_19.txt", "w")
       text = (self.driver.find_element(By.XPATH, "/html/body").text)
       f.write(text)
       f.close()
       self.driver.close()


webpage = Guvi()
webpage.webpage_details()
webpage.print_page_text_file()
