from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки клавиатуры админа
button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')

buton_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)
buton_case_admin.add(button_load)
buton_case_admin.add(button_delete)
