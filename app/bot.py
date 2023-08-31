from aiogram import Bot, Dispatcher, executor
from app.settings import Settings


class App:
    bot = Bot(Settings.TOKEN)
    dp = Dispatcher(bot)

