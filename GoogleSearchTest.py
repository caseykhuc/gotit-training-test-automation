import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        base_url = "https://google.com"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(.5)

        # Launch
        self.driver.maximize_window()
        self.driver.get(base_url)
        # self.main_window = self.driver.current_window_handle

    def test(self):
        driver = self.driver
        # Search
        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.send_keys("Random keyword")

        # Submit
        search_bar.submit()

        # Validate Url
        self.assertTrue("q=Random+keyword" in driver.current_url)

        # Open the first result on new tab
        first_result = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.r>a')))
        GoogleSearchTest.open_link(driver, first_result)

        time.sleep(1)

    @staticmethod
    def open_link(driver, obj):
        ActionChains(driver) \
            .move_to_element(obj) \
            .key_down(Keys.COMMAND) \
            .click(obj) \
            .key_up(Keys.COMMAND) \
            .perform()

        # Switch to the result - next tab on the right
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[len(window_handles) - 1])
        print(driver.title)
        time.sleep(1)

        # Close current tab
        driver.close()


if __name__ == '__main__':
    unittest.main()
