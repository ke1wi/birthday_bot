import os
from app.bot import App
from app.settings import Settings
from aiogram import executor, types
from app.logic import Logic

async def rm(dp):
    os.remove("table/table_for_bot.csv")

@App.dp.message_handler(commands=['checkdr'], commands_prefix=['~'])
async def check_dr(msg: types.Message):
    await App.bot.send_message(Settings.ADMIN_ID, Logic.check())
    
@App.dp.message_handler(commands=['sendcong'], commands_prefix=['~'])
async def congrats(msg: types.Message):
    await App.bot.send_message(Settings.CHAT_ID, Logic.send_congrats())




executor.start_polling(App.dp, skip_updates=True, on_startup=check_dr, on_shutdown=rm)