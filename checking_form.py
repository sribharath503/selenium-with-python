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




#another method but not working chatgpt gives...
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Define the URL of your local HTML file
url = "http://127.0.0.1:5500/week1.html"  # Update this path if necessary

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(url)

# Locate elements by their IDs
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_btn = driver.find_element(By.ID, "loginBtn")
cancel_btn = driver.find_element(By.ID, "cancelBtn")

# Input data into the fields
username.send_keys("bharath")
password.send_keys("12345")

# Simulate clicking the Login button
login_btn.click()
time.sleep(2)

# Clear the input fields
username.clear()
password.clear()

# Simulate clicking the Cancel button
cancel_btn.click()
time.sleep(2)

# Keep the browser open for a while to observe
time.sleep(10)

# Close the browser
#driver.quit()
'''