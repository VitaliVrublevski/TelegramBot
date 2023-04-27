from aiogram.utils import executor
from create_bot import dp
from handlers import client, other, admin
import logging
from data_base import sqllite_db

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print('Бот вышел в онлайн')
    sqllite_db.sql_start()


def register_handlers():
    client.register_handlers(dp)
    admin.register_handlers(dp)
    other.register_handlers(dp)


if __name__ == '__main__':
    register_handlers()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
