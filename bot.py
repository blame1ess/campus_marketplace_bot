import logging
from aiogram import Bot, Dispatcher, executor, types

import reply as nav
import inline as inl

API_TOKEN = '5214367976:AAE70RfU32o_UjpOgDegVxUAVsxNFepywkQ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def bot_message(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open('mainphoto.jfif', 'rb'))
    await bot.send_message(message.from_user.id, 'Добро Пожаловать в Ethanol Delivery! 🥂\n\n--- бесплатная доставка от 1200тг ---\n'
                                                 '--- стоимость доставки - 100тг ---\n\n '
                                                 '--- ❗️просим соблюдать все инструкции ❗️ ---\n\n Гайд:\n '
                                                 '1) Смотрите меню, выбираете товар\n\n'
                                                 '2) Пишете в личку(telegram) на номер: +7 778 189 5555 по форме ниже:\n'
                                                 'Имя, номер блока/комната, продукт - кол.во, продукт - кол.во ....\n\n'
                                                 'пример:\n'
                                                 '"Хулио, 55/555, Жатецки - 2, Сомерс Манго - 3, Lays/Paprika - 1 ..."\n\n'
                                                 '3) Получаете сообщение от оператора ✅✅✅\n\n\n'
                                                 'По всем вопросам:\n\n'
                                                 '8️⃣  7️⃣7️⃣8️⃣  1️⃣8️⃣9️⃣  5️⃣5️⃣5️⃣5️⃣\n\n'
                                                 '@ethanol_delivery',
                           reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Меню':
        await message.reply("Наше меню:", reply_markup=inl.main_inl)



# Inline buttons ------------
#Vodka
@dp.callback_query_handler(text=["vodka_price"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "vodka_price":
        await call.message.reply('Выберите водку', reply_markup=inl.vodka_inl)
    await call.answer()

@dp.callback_query_handler(text=["sg5"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "sg5":
        await call.message.reply('Выберите действие', reply_markup=inl.sg5_inl)
    await call.answer()

@dp.callback_query_handler(text=["back"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "back":
        await call.message.reply('Возвращаемся назад', reply_markup=inl.main_inl)
    await call.answer()

@dp.callback_query_handler(text=["mainmenu"])
async def main_menu_btn(call: types.CallbackQuery):
    if call.data == "mainmenu":
        await call.message.reply('Возвращаемся на главное меню', reply_markup=inl.main_inl)
    await call.answer()

@dp.callback_query_handler(text=["basket"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "basket":
        await call.message.reply('Синяя гора(1) добавлено в корзину', reply_markup=inl.vodka_inl)
    await call.answer()

@dp.callback_query_handler(text=["buy_now"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "buy_now":
        await call.message.reply('Выберите блок', reply_markup=inl.block_inl)
    await call.answer()

# ----- Блоки(НУ) ------

@dp.callback_query_handler(text=["22"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "22":
        await call.message.reply('Выберите этаж:', reply_markup=inl.stage_inl)
    await call.answer()

@dp.callback_query_handler(text=["23"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "23":
        await call.message.reply('Выберите этаж:', reply_markup=inl.stage_inl)
    await call.answer()

@dp.callback_query_handler(text=["24"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "24":
        await call.message.reply('Выберите этаж:', reply_markup=inl.stage_inl)
    await call.answer()

@dp.callback_query_handler(text=["25"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "25":
        await call.message.reply('Выберите этаж:', reply_markup=inl.stage_inl)
    await call.answer()

@dp.callback_query_handler(text=["26"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "26":
        await call.message.reply('Выберите этаж:', reply_markup=inl.stage_inl)
    await call.answer()

@dp.callback_query_handler(text=["27"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "27":
        await call.message.reply('Выберите этаж:', reply_markup=inl.stage_inl)
    await call.answer()
# ---- end -------

# ---- этаж ------
@dp.callback_query_handler(text=["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
async def vodka_menu(call: types.CallbackQuery):
    if call.data == "2" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12":
        await call.message.reply('Выберите комнату:', reply_markup=inl.room_inl)
    await call.answer()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)

