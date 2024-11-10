from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException


url = "http://127.0.0.1:5500/week1.html"

driver=webdriver.Chrome()
driver.get(url)

username=driver.find_element(By.ID, "username")
password=driver.find_element(By.ID, "password")

username.send_keys("bharath")
password.send_keys("12345")


try:
    search_box = driver.find_element(By.ID, "loginBtnn")
    search_box.send_keys(Keys.RETURN)
except NoSuchElementException:
    print("__no such id is occurs__")



time.sleep(1000)

#driver.quit()

