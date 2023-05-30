# Automated python login script using selenium library

# Necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Setting up options, i needed that to keep my window from closing
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

# Initializing driver with university login page
url = "<loginUrl>"
driver.get(url)

# Fiding input forms
login = driver.find_element(By.ID, 'login')
passwd = driver.find_element(By.ID, 'password')
OK = driver.find_element(By.CLASS_NAME, 'success')

# Filling input forms
login.send_keys("<username>")
passwd.send_keys("<password>")
OK.click()

# Closing
driver.close()
