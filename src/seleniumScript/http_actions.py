import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.settings.settings import SettingsManager

from src.utils.utils import generate_random_email, generate_random_name

from src.mtsAPI.api_request import OnlineSimHandler


class SeleniumBot:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.client = OnlineSimHandler()
        self.url = url

    def enter_email(self) -> None:
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        submit_button = self.driver.find_element(By.ID, "submit")

        name_input.send_keys(generate_random_name())
        email_input.send_keys(generate_random_email())
        submit_button.click()
        return

    def enter_phone_number(self):
        self.driver.get(self.url)
        phone_input = self.driver.find_element(By.NAME, "phone")
        phone_input.click()

        number = self.client.get_new_number()
        number_for_input = number[2:]

        phone_input.send_keys(number_for_input)

        element = self.driver.find_element(By.ID, "submitButton")
        element.click()
        return number

    def enter_input_code(self, number):
        time.sleep(7)
        msg_code = self.client.get_rented_number_message(number)

        for elem in range(4):
            element = self.driver.find_element(
                    By.NAME,
        f"form[verificationCodeDigits][{elem}]")
            element.click()

            element.send_keys(msg_code[elem])

        element = self.driver.find_element(By.ID, "form-submit")
        element.click()

    def run(self):
        number = self.enter_phone_number()
        self.enter_input_code(number)
        self.enter_email()
