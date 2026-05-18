from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT = "natgeo"
USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(USERNAME)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            not_now = self.driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]")
            not_now.click()
        except:
            pass

        time.sleep(3)

        try:
            not_now2 = self.driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]")
            not_now2.click()
        except:
            pass

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(3)

        modal = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                if button.text == "Follow":
                    button.click()
                    time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Cancel')]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()