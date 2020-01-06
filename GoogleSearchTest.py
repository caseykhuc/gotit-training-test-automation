from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time


class GoogleSearchTest:
    @staticmethod
    def test():
        base_url = "https://google.com"
        driver = webdriver.Chrome()
        driver.implicitly_wait(.5)
        # Launch
        driver.maximize_window()
        driver.get(base_url)

        # Search
        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.send_keys("Random keyword")

        # Submit
        search_bar.submit()

        # Validate Url
        if "q=Random+keyword" not in driver.current_url:
            raise Exception("Invalid Url")

        # Click on the first result
        first_result = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '(//div[@class="r"])[1]/a')))
        first_result.click()

        WebDriverWait(driver, 5).until_not(
            EC.presence_of_element_located((By.XPATH, '(//div[@class="r"])[1]/a')))


ff = GoogleSearchTest()
ff.test()
