from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

# ,"thedevlife","programunity","jeffnippard"}
SIMILAR_ACCOUNT="peoplewhocode"
USERNAME="josko.fit"
PASSWORD="sifrasifra"

class InstaFollower:
    def __init__(self):
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=chrome_options)

    def login(self):
        url="https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.3)

        decline_cookies_xpath="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning=self.driver.find_elements(By.XPATH, decline_cookies_xpath)

        if cookie_warning:
            cookie_warning[0].click()

        username=self.driver.find_element(by=By.NAME, value="username")
        password=self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2.1)
        password.send_keys(Keys.ENTER)

        time.sleep(4.3)
        save_login_prompt=self.driver.find_element(by=By.XPATH,value="//div[contains(text(), 'Ne sada')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        # notifications_prompt=self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Ne sada')]")
        # if notifications_prompt:
        #     notifications_prompt.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(3.5)
        followers = self.driver.find_element(By.CSS_SELECTOR, value="div.x40hh3e:nth-child(3) > div:nth-child(2) > a:nth-child(1)")
        followers.click()
        time.sleep(2)
        # modal = self.driver.find_element(By.CLASS_NAME, value="xyi19xy")
        # modal = self.driver.find_element(By.XPATH, value="/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        modal = self.driver.find_element(By.CSS_SELECTOR, value="body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.x15fl9t6.x1yw9sn2.x1evh3fb.x4giqqa.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.x6nl9eh.x1a5l9x9.x7vuprf.x1mg3h75.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6")
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons=self.driver.find_elements(By.CSS_SELECTOR, value='div.x1qnrgzn:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)

            except ElementClickInterceptedException:
                cancel_button=self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot=InstaFollower()
bot.login()
bot.find_followers()
bot.follow()