from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from packaging import version
import time


class EnterData:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 15)

    def input_data(self, all_address, all_price, all_links):
        self.driver.get("https://forms.gle/HwgqJS8VCkLnBpxQ6")

        # get the element tag and input their values
        address = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.zHQkBf")))[0]
        address.send_keys(all_address)

        price = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.zHQkBf")))[1]
        price.send_keys(all_price)

        link = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.zHQkBf")))[2]
        link.send_keys("https://nigeriapropertycentre.com"+all_links)

        button = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
        button.click()

        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Submit another response"))).click()
