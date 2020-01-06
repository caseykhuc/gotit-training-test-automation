import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PurchaseExcelchat(unittest.TestCase):
    def setUp(self):
        base_url = "https://www.got-it.tech/solutions/excel-chat"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(.5)

        # Launch
        self.driver.maximize_window()
        self.driver.get(base_url)

    def test(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Login
        driver.find_element(By.ID, "test-login-button").click()
        log_in_modal = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="modal-login"]'))
        )

        log_in_modal.find_element(
            By.XPATH, '//input[@name="email"]'
        ).send_keys("trang+99@gotitapp.co")

        log_in_modal.find_element(
            By.XPATH, '//input[@name="password"]'
        ).send_keys("1234aA")

        log_in_modal.find_element(
            By.XPATH, '//button[@id="login-button"]'
        ).click()

        # Navigate to Pricing page
        wait.until_not(
            EC.presence_of_element_located((By.XPATH, '//*[@id="modal-login"]'))
        )
        driver.find_element(By.ID, 'pricing-navlink-landing').click()

        # Invoke payment modal
        unlimited_sessions_option = driver.find_element(By.CSS_SELECTOR, "div.gi-coverPricing-Inner div.gi-pricingItem")\
            .find_element(By.XPATH, '//div[text()="Unlimited Sessions"]/parent::div')
        unlimited_sessions_option.find_element(By.CSS_SELECTOR, "div.gi-pricingItem-Button").click()

        # Handle payment method
        payment_modal = wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'div.modal-content'
            )))
        try:
            methods = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.braintree-loaded div.braintree-method'))
            )
            methods.find_element(By.XPATH, '//div[contains(text(), "1881")]').click()

        except NoSuchElementException:
            payment_modal.find_element(
                By.XPATH, '//span[text()="Choose another way to pay"]'
            ).click()
            payment_modal.find_element(By.CSS_SELECTOR, 'div.braintree-option__card').click()
        finally:
            payment_modal.find_element(By.CSS_SELECTOR, 'div.modal-footer button.gi-Button').click()
            """wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'div.modal-content iframe[title="purchase-success"]')
                )
            )"""
            # assert something

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
