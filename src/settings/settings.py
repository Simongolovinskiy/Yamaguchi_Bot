from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "../.env"))


class SettingsManager:

    @staticmethod
    def get_api_key():
        return os.getenv("API_KEY")

    @staticmethod
    def get_online_sim_balance_url():
        return os.getenv("BALANCE_URL")

    @staticmethod
    def get_new_number_url():
        return os.getenv("NEW_NUMBER_URL")

    @staticmethod
    def get_tariff_url():
        return os.getenv("TARIFF_URL")

    @staticmethod
    def get_state_url():
        return os.getenv("GET_STATE")

    @staticmethod
    def get_bot_token():
        return os.getenv("BOT_TOKEN")
