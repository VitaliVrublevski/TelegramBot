from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqllite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приветствую Вас.', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/VitaRobot_bot')


# @dp.message_handler(commands=['Адрес'])
async def vita_address_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'г.Лида, ул. Толстого 26', reply_markup=ReplyKeyboardRemove())


async def vita_menu_command(message: types.Message):
    await sqllite_db.sql_read(message)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(vita_address_command, commands=['Адрес'])
    dp.register_message_handler(vita_menu_command, commands=['Меню'])
