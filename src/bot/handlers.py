from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import re

from src.seleniumScript.http_actions import SeleniumBot
from src.mtsAPI.api_request import OnlineSimHandler

router = Router()

url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Здравствуйте! Введите ссылку на креслице :-)")


@router.message()
async def message_handler(msg: Message):
    text = msg.text
    match = re.search(url_pattern, text)
    if match:
        check_balance = OnlineSimHandler()
        if not check_balance.check_for_buy():
            await msg.answer("У вас недостаточно денег на счету вашего кошелька с симками :-(")

        url = match.group()
        await msg.answer(f"Вы ввели ссылку: {url}, ждите 15-20 секунд и желаем вам приятного массажа :-)")
        try:
            script = SeleniumBot(url)
            script.run()
            await msg.answer("Приятного массажа :-)")
        except:
            await msg.answer("Некорректная ссылка, введите, пожалуйста, еще раз :-(")
    else:
        await msg.answer("Текст сообщения не содержит ссылку :-(")

