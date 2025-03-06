import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options

driver = webdriver.Edge()
#driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/iframe")

alert = Alert(driver)

alert.accept() # Click ok
alert.dismiss() # Click cancel

#*************************** Keyboard keys actions *************************

input_box = driver.find_element(By.ID, "#username")
input_box.send_keys("subbarma")

input_box.send_keys(Keys.ENTER)

#*************************** Headless mode *************************

option = Options()
option.add_argument("--headless") # it will run in headless mode

# download the files

option.experimental_options("pref", {"download.default_directory": "C:\\Downloads",
                                     "download.prompt_for_download": False})

driver.webdriver.Chrome(option=Options)
driver.get("http://example.com/download")

#*************************** JavaScript in selenium *************************

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # It can scroll to bottom of the page

element = driver.find_element(By.ID, "button")
driver.execute_script("arguments[0].click();", element)  # click using javascript
text = driver.execute_script("returnargument[0].innerText;", element) # taking text using javascript
print(text)
