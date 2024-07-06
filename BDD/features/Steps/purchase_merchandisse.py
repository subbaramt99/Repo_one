from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@given('I am on the Demo Login Page')
def Demo_Login(context):
    context.driver = webdriver.Edge()
    context.driver.get("https://www.saucedemo.com/")
    print("Url launched successfully")

@when('I fill the account information for account StandardUser into the Username field and the Password field')
def filling_userCredentials(context, username, password):
    #context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys("standard_user")
    context.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("secret_sauce")
    print("user credentials entered successfully")

@when('I click the Login Button')
def clicking_LoginBtn(context):
    context.driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()
    print("user logged in successfully")

@then('I am redirected to the Demo Main Page')
def In_demoMain_page(context):
    assert context.driver.title == "Swag Labs"
    print("I verified I'm in demo main page")

@then('I verify the App Logo exists')
def step_impl(context):
    Logo = context.driver.find_element(By.XPATH, "//div[@class = 'app_logo']").is_displayed()
    assert Logo == True
    print("I verified the app logo")

@when('I fill the account information for account LockedOutUser into the Username field and the Password field')
def LockedOutUser(context):
    context.driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys("locked_out_user")
    context.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("secret_sauce")
    #context.driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()
    #print("user logged in successfully")

@then('I verify the Error Message contains the text "Sorry, this user has been banned. "')
def Verifying_Error(context):
    ErMsg = context.driver.find_element(By.XPATH, "//button[@class = 'error-button']").text
    assert "Sorry, this user has been locked out." in ErMsg
    #raise NotImplementedError(u'STEP: Then I verify the Error Message contains the text "Sorry, this user has been banned. "')


@given('I am on the inventory page')
def Inventory_Page(context):
    context.driver = webdriver.Edge()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys("standard_user")
    context.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("secret_sauce")
    context.driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()



@when('user sorts products from low price to high price')
def sorting_price(context):
    static_dropdown = Select(context.driver.find_element(By.XPATH, "//select[@class = 'product_sort_container']"))
    static_dropdown.select_by_index(2)
    #raise NotImplementedError('STEP: When user sorts products from low price to high price')
    print("user sorted the products from low price to high price")

@when('user adds lowest priced product')
def added_LowPrice_product(context):
    prices = context.driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_price']")
    cost = []
    for price in prices:
        cost.append(price.text)
    print(cost)


@when('user clicks on cart')
def add_to_cart(context):
    context.driver.find_elements(By.XPATH, "//button[@class = 'btn btn_primary btn_small btn_inventory ']").click()
    print("user added minimum value product")

@when('user clicks on checkout')
def goto_cart(context):
    context.driver.find_element(By.XPATH, "//div/a[@class = 'shopping_cart_link']").click()
    context.driver.find_element(By.XPATH, "//button[@class = 'btn btn_action btn_medium checkout_button ']").click()

@when('user enters first name John')
def entering_firstName(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder = 'First Name']").send_keys("John")


@when('user enters last name Doe')
def entering_lastName(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder = 'Last Name']").send_keys("Doe")

@when('user enters zip code 123')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder = 'Zip/Postal Code']").send_keys("123")

@when('user clicks Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

@then('I verify in Checkout overview page if the total amount for the added item is $8.63')
def verfy_totlAmt(context):
    total = context.driver.find_element(By.XPATH, "//div[@class = 'summary_total_label']").text
    print(total)
    assert "8.63" in total
    print("Total price is verified the added item is $8.63")

@when('user clicks Finish button')
def Clicking_finish(context):
    context.driver.find_element(By.XPATH, "//button[@id = 'finish']").click()

@then('Thank You header is shown in Checkout Complete page')
def checkout_complete(context):
    complete_order = context.driver.find_element(By.XPATH, "//div/h2[@class = 'complete-header']").text
    print(complete_order)
    assert "Thank you for your order!" == complete_order