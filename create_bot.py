from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv

import os

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
