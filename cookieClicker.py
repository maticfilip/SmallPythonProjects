from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import with_tag_name

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)
language=driver.find_element(By.ID, value="langSelect-EN")
language.click()



time.sleep(2)
cookie=driver.find_element(By.ID, value="bigCookie")
cookie_count=driver.find_element(By.ID, value="cookies")
item_ids=[f"product{i}" for i in range(18)]

wait_time=5
timeout=time.time()+wait_time
five_min=time.time()+60*5

while True:
    cookie.click()

    if time.time()>timeout:
        try:
            cookies=driver.find_element(by=By.ID, value="cookies")
            cookie_text=cookies.text
            cookie_count=int(cookie_text.split()[0].replace(",",""))

            products=driver.find_elements(by=By.CSS_SELECTOR,value="div[id^='product']")

            best_item=None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item=product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except(NoSuchElementException,ValueError):
            print("Couldn't find cookie count or items.")

        timeout=time.time()+wait_time

    if time.time()>five_min:
        try:
            cookies=driver.find_element(By.ID, value="cookies")
            print(f"Final result: {cookies.text}")
        except NoSuchElementException:
            print("Couldn't")
        break