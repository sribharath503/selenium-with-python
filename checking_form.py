from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "http://127.0.0.1:5500/week1.html"

driver=webdriver.Chrome()
driver.get(url)

username=driver.find_element(By.ID, "username")
password=driver.find_element(By.ID, "password")

username.send_keys("bharath")
password.send_keys("12345")

search_box = driver.find_element(By.ID, "loginBtn")
search_box.send_keys(Keys.RETURN)


time.sleep(1000)

#driver.quit()

