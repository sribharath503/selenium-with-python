# Import Selenium WebDriver
from selenium import webdriver

# Specify the path to the ChromeDriver
# If ChromeDriver is not in your system PATH, provide the exact path to the driver

url = "https://www.flipkart.com/"

# Open Google
driver = webdriver.Chrome()
driver.get(url)

# Print the title of the current webpage
print("Page Title is: ", driver.title)

# Close the browser
driver.quit()
