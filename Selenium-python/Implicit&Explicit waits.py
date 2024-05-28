import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.implicitly_wait(4)  # 4sec is max time out...if the object find in 2 sec (3 sec is saved)


def webdriverwait(driver, param):
    pass


class Implicit_Explicit_waits(object):
    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    search = "//input[@type ='search']"
    CartBtn2 = "//div/div/a[@class = 'cart-icon']"
    CartBtn1 = "//img[@alt = 'Cart']"
    ChecoutBtn = "//div/div/div/button"
    PromoCode = ".promocode"
    Applyofr = ".promoBtn"
    PromoInfo = ".promoInfo"
    BuildingNum = "232"

    driver.find_element(By.XPATH, search).send_keys("b")
    print("searching done")
    time.sleep(1)
    results = driver.find_elements(By.XPATH, "//div[@class ='products']/div")
    resultsOfProductsName = driver.find_elements(By.XPATH, "//div[@class ='products']/div/h4")
    time.sleep(2)
    NumOfProduct = len(results)
    print("Number of products:", NumOfProduct)
    productlist = []
    for result in results:
        result.find_element(By.XPATH, "div/button").click()
        productlist.append(result.find_element(By.XPATH, "h4").text)
        time.sleep(1)
    print("All Products added in cart")
    driver.find_element(By.XPATH, CartBtn1).click()
    # time.sleep(1)
    print("Clicked in My cart")
    driver.find_element(By.XPATH, ChecoutBtn).click()
    # time.sleep(3)
    print("Clicked on proceed to checkout")
    driver.find_element(By.CSS_SELECTOR, PromoCode).send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR, Applyofr).click()

    #driver.implicitly_wait(self, time to wait)

    # Important Note for explicit wait
    wait = WebDriverWait(driver, 10)   # Explicit wait means the control wait for that particular action
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))


    print("Offer applied successfully")
    print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
    assert (driver.find_element(By.CSS_SELECTOR, ".promoInfo").text) == "Code applied ..!"
    # print(driver.find_element(By.XPATH, "//div/div/span[@class = 'promoInfo']").text)
    # assert (driver.find_element(By.XPATH, "//div/div/span[@class = 'promoInfo']").text) == "Code applied ..!"
    print("Calculated total money")
    prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
    productName = driver.find_elements(By.XPATH, "//tr/td[2]/p")
    sum =0
    for price in prices:
        sum = sum + int(price.text)
    print("Total", sum)
    print(productlist)
    totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totamt").text)
    print("Total Amount is:", totalAmount)

    DiscountAmt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
    print("Discounted Amount is:", DiscountAmt)

    assert sum == totalAmount
    print("Calculated amount correct")
    assert DiscountAmt < totalAmount
    print("discount applied successfully")

    print("Selected the building number", +int(BuildingNum))


