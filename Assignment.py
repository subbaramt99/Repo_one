import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.implicitly_wait(4)    # Implicit wait
def Assignment():
    #driver.implicitly_wait(4)
    password = "1234567"
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(4)
    driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

    openWindows = driver.window_handles  # New windows handlling
    driver.switch_to.window(openWindows[1])


    loginID = driver.find_element(By.XPATH, "//a[@href = 'mailto:mentor@rahulshettyacademy.com']").text
    print(loginID)

    openWindows = driver.window_handles
    driver.switch_to.window(openWindows[0])  #Return back to old opened windows


    driver.find_element(By.XPATH, "//input[@name = 'username']").send_keys(loginID)
    #time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id= 'terms']").click()
    #time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id= 'signInBtn']").click()
    #time.sleep(4)
    driver.find_element(By.XPATH, "//div[@class= 'alert alert-danger col-md-12']")

    driver.find_element(By.CSS_SELECTOR, ".alert-danger")
    wait = WebDriverWait(driver, 10)  # Explicit wait
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
#    errorMsg = driver.find_element(By.XPATH, "//strong").text
#    print(errorMsg)



Assignment()
