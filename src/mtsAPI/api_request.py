import requests
import json

from src.settings.settings import SettingsManager


class OnlineSimHandler:
    def __init__(self):
        self.api_key = SettingsManager.get_api_key()

    def get_balance(self):
        request = requests.get(
            url=SettingsManager.get_online_sim_balance_url(),
            params={"apikey": self.api_key}
        )
        response = json.loads(request.text)
        return float(response["balance"])

    def get_country_code(self):
        request = requests.get(
            url=SettingsManager.get_tariff_url(),
            params={"apikey": self.api_key}
        )
        response = json.loads(request.text)
        return response["countries"]["_7"]["code"]

    def get_service(self):
        request = requests.get(
            url="https://onlinesim.io/api/getTariffs.php",
            params={"apikey": self.api_key,
                    "filter_service": "yamaguchi"}
        )

        return json.loads(request.text)["services"]["_yamaguchi"]["slug"]

    def get_price(self):
        request = requests.get(
            url="https://onlinesim.io/api/getTariffs.php",
            params={"apikey": self.api_key,
                    "filter_service": "yamaguchi"}
        )

        return float(json.loads(request.text)["services"]["_yamaguchi"]["price"])

    def check_for_buy(self):
        if float(self.get_balance()) < float(self.get_price()):
            return False
        return True

    def get_new_number(self):

        self.check_for_buy()

        request = requests.get(
            url=SettingsManager.get_new_number_url(),
            params={
                "apikey": self.api_key,
                "country": self.get_country_code(),
                "service": self.get_service()
                }
        )
        response = json.loads(request.text)

        id = response["tzid"]
        number_req = requests.get(
            url=SettingsManager.get_state_url(),
            params={
                "apikey": self.api_key
            }
        )
        for number in json.loads(number_req.text):
            if id == number["tzid"]:
                return number["number"]

    def get_rented_number_message(self, number):
        request = requests.get(
            url=SettingsManager.get_state_url(),
            params={
                "apikey": self.api_key
            }
        )
        response = json.loads(request.text)

        for numbers in response:
            if number == numbers["number"]:
                return numbers.get("msg")

