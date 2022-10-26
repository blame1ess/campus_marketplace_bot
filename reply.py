from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# -- main menu --
btnMenu = KeyboardButton('Меню')
btnBasket = KeyboardButton('Корзина')
btnInfo = KeyboardButton('Info')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMenu, btnBasket, btnInfo)








