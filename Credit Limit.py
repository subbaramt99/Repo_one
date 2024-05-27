import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service_obj = Service("C:\SUBBARAM T\Applications\selenium\chromedriver-win64\chromedriver-win64")
#driver = webdriver.Chrome(Service = service_obj)
# driver.get("https://gmail.com")
envModA = "//input[@name='env'][1]"
envModC = "//input[@name='env'][3]"
customerName = "//input[@name='cus_name']"
CUGID = "CUG4500147734"
leCode = "//input[@name='le_code']"
LECODE = "4500027289"
limit = "//input[@name='risk_limit']"
submit = "//button[@name='submit']"
# service_obj = Service #seleniumManager
# driver = webdriver.Chrome(service = service_obj)
# driver = webdriver.Chrome()
driver = webdriver.Edge()
try:
    driver.get("http://10.54.10.2:61001/Mecrd_credit_limit_V1_1/index.jsp")
    print(driver.title)
    print(driver.current_url)
    print("Url loaded successfully")
except Exception as e:
    raise e
#driver.get("https://cust-test-login.secure-test.btintra.com/login.fcc?TYPE=33554433&REALMOID=06-6733d2ea-494d-10b0-97bc-843bdb4e0cb3&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=$SM$%2b8SsXTecO%2fN1x2VybxeGRhBTEkdi53%2frg%2blA8g%2fwrsvLjCxJ6Bk4GbYrebEd3rEuf0lGlL%2f3BrpJs5zVuGmOI0w%2bhQVqPkW4&TARGET=$SM$HTTP:%2f%2fec-saasukb-e2e-hd.nat.bt.com%2fclient.aspx")

driver.minimize_window()
time.sleep(2)
try:
    driver.find_element(By.XPATH, "//input[@value='mod_a']").click()
    time.sleep(2)
    print("Environment selected")
except Exception as e:
    raise e

try:
    driver.find_element(By.XPATH, "//input[@name='cus_name']").send_keys(CUGID)
    time.sleep(2)
    print("CUG ID entered successfully")
except Exception as e:
    raise e

try:
    driver.find_element(By.NAME, "le_code").send_keys(LECODE)
    time.sleep(2)
    print("LeCode entered successfully")
except Exception as e:
    raise e

try:
    driver.find_element(By.XPATH, "//input[@name='risk_limit']").send_keys("100000")
    time.sleep(2)
    print("Credit Limit entered successfully")
except Exception as e:
    raise e

try:
    driver.find_element(By.XPATH, "//button[@name='submit']").click()
    time.sleep(5)
    print("Submitted  successfully")
except Exception as e:
    raise e


# driver.find_element(By.NAME, "submit").click()

# Syntax of Xpath
# Xpath --> //tagname[@attribute='value']
# CSS selector --> tagname[attribute='value']

# driver.find_element(By.XPATH, "//input[@id='username']").send_keys("920191895")
# driver.find_element(By.ID, "username").send_keys("920191895")
#driver.find_element(By.CSS_SELECTOR,"input[id='username']").send_keys("920191895")
#driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Agdt@1234567")
# driver.find_element(By.LINK_TEXT,"Can't access your account?").click()
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
