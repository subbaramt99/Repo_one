import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#from ChromeOptionsDemo import driverOptions


class AngularPractice:
    #Driver_Options = driverOptions
    driver_options = webdriver.EdgeOptions()
    driver_options.add_argument("--start-maximized")  # Browser will start with maximized screen

    driver = webdriver.Edge(options=driver_options)
    driver.implicitly_wait(5)
    AngularPracticeUrl = "https://rahulshettyacademy.com/angularpractice/"
    Shopbtn = "//li/a[@href= '/angularpractice/shop']"
    Shopbtn2 = "//li/a[text() = 'Shop']"
    Items = "//div[@class = 'card h-100']"
    AddBtn = "div/button[@class = 'btn btn-info']"   # Important Note If we route from parent to child with chain
    # should be like XPATH "//"
    CheckoutBtn1 = "//div/ul/li/a[@class = 'nav-link btn btn-primary']"
    CheckoutBtn2 = "//button[@class='btn btn-success']"
    AutoSugDrpdwn = "//input[@id = 'country']"

    driver.get(AngularPracticeUrl)
    driver.find_element(By.XPATH, Shopbtn).click()
    Products = driver.find_elements(By.XPATH, Items)
    #print(Products)
    for product in Products:
        ProductName = product.find_element(By.XPATH, "div/h4/a").text
        print(ProductName)
        if ProductName == "Blackberry":
            print("Blackberry founded")
            product.find_element(By.XPATH, "div/button[@class = 'btn btn-info']").click()
            # Chain xpath should not be like usual XPATH "//" missing here
    #time.sleep(3)
            #driver.get_screenshot_as_file("checkoutScrn12.png")
    driver.find_element(By.XPATH, CheckoutBtn1).click()
    driver.execute_script("window.scroll(0,0)")
    #time.sleep(2)
    driver.get_screenshot_as_file("checkoutScrn1.png")
    #time.sleep(2)
    #driver.get_screenshot_as_file("checkoutScrn.png")
    driver.find_element(By.XPATH, CheckoutBtn2).click()
    # for finding CSS selector using xpath go to console in browser write $x("XPATH") enter
    #it will give the CSS selector of the xpath.
    #driver.find_element(By.CSS_SELECTOR, "[button.btn.btn-success]").click()
    driver.find_element(By.XPATH, AutoSugDrpdwn).send_keys("IND")
    countries = driver.find_elements(By.XPATH, "//div[@class = 'suggestions']/ul/li/a")
    # The above Xpath should have finding of entered values ex: India, Indonesia...
    #time.sleep(2)
    SugCountries = []
    #for country in countries:
        # SugCountries.append(country.text)  # storing the suggestion into new list
        #if country.text == "India":
            #country.find_element(By.LINK_TEXT, "India") # Uanbel to perform click action here
        #print(country.text)
        #driver.find_element(By.LINK_TEXT, "India").click()

    wait = WebDriverWait(driver,10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()

    driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click() # using CSS selector to locate the element

    driver.find_element(By.XPATH, "//input[@type = 'submit']").click()  # Using CSS selectortor locate the element
    #driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    SuccessText = driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']").text
    print(SuccessText)
    #assert "Success" == SuccessText  # It will fail because it expect exact match of text
    # SuccessText is "Success! Thank you! Your order will be delivered in next few weeks :-)."
    assert "Success!" in SuccessText  # It will check if match the text
