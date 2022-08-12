import time

import selenium
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True) #do not close window at end of execution
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


# time.sleep(2)
# lang_select = driver.find_element(By.ID, 'langSelect-EN')
# lang_select.click()
#
# driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]').click()
cookie = driver.find_element(By.ID, 'cookie')
#get all children of store element
store = driver.find_element(By.ID, 'store')
store_items = store.find_elements(By.CSS_SELECTOR, '*')
store_unavailable = store.find_elements(By.CLASS_NAME, 'greyed')

# ###########STORE
# cursor = driver.find_element(By.ID, 'buyCursor')
# grandma = driver.find_element(By.ID, 'buyGrandma')
# factory = driver.find_element(By.ID, 'buyFactory')

while True:
    cookie.click()
    store = driver.find_element(By.ID, 'store')
    store_items = store.find_elements(By.CSS_SELECTOR, '*')
    del store_items[-1]
    store_unavailable = store.find_elements(By.CLASS_NAME, 'greyed')
    cookie.click()
    for item in store_items:
       # item_id = item.get_attribute("id")

        try:
            cookie.click()
            #item_amount = int(item.find_element(By.CLASS_NAME, 'amount').text)
            item.click()


            #item = WebDriverWait(driver, 4, ignored_exceptions=StaleElementReferenceException).until(expected_conditions.presence_of_element_located((By.ID, item_id)))
        except selenium.common.exceptions.ElementNotInteractableException:
            cookie.click()
            continue
        except StaleElementReferenceException:
            cookie.click()
            continue
        except selenium.common.exceptions.NoSuchElementException:
            cookie.click()
            continue



