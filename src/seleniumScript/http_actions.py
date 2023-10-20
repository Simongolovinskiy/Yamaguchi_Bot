import time

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

    def number_page(self) -> None:
        self.driver.get(self.url)
        element = self.driver.find_element(By.XPATH, "//*[text()='Бесплатно 10 мин']")
        element.click()
        element = self.driver.find_element(By.LINK_TEXT, "Зарегистрироваться")
        element.click()

    def enter_registration_data(self):
        name_input = self.driver.find_element(By.NAME, "name")
        email_input = self.driver.find_element(By.NAME, "email")
        phone_input = self.driver.find_element(By.NAME, "phone")

        number = self.client.get_new_number()

        name_input.send_keys(generate_random_name())
        email_input.send_keys(generate_random_email())
        phone_input.send_keys(number)
        element = self.driver.find_element(By.ID, "submit")
        element.click()
        return number

    def receive_input_code(self, number):
        time.sleep(5)
        msg_code = self.client.get_rented_number_message(number)
        element = self.driver.find_element(By.NAME, "verificationCode")
        element.send_keys(msg_code)
        element = self.driver.find_element(By.NAME, "submit")
        element.click()

    def run(self):
        self.number_page()
        number = self.enter_registration_data()
        self.receive_input_code(number)

