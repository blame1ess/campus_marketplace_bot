from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn1 = InlineKeyboardButton(text="Vodka", callback_data="vodka_price")
btn2 = InlineKeyboardButton(text="Beer", callback_data="beer_price")
btn3 = InlineKeyboardButton(text="Wine", callback_data="wine_price")

main_inl = InlineKeyboardMarkup().add(btn1, btn2, btn3)

# common buttons

main_m = InlineKeyboardButton(text="Главное меню", callback_data="mainmenu")

#vodka menu

btn4 = InlineKeyboardButton(text="Синяя гора - 2400 тг", callback_data="sg5")

vodka_inl = InlineKeyboardMarkup().add(btn4)

#sg5 menu (5-7)

btn5 = InlineKeyboardButton(text="Добавить в корзину", callback_data="basket")
btn6 = InlineKeyboardButton(text="Купить сейчас", callback_data="buy_now")
btn7 = InlineKeyboardButton(text="Назад", callback_data="back")    # common button
sg5_inl = InlineKeyboardMarkup().add(btn5, btn6, btn7)

#block menu (8-13)

btn8 = InlineKeyboardButton(text="22", callback_data="22")
btn9 = InlineKeyboardButton(text="23", callback_data="23")
btn10 = InlineKeyboardButton(text="24", callback_data="24")
btn11 = InlineKeyboardButton(text="25", callback_data="25")
btn12 = InlineKeyboardButton(text="26", callback_data="26")
btn13 = InlineKeyboardButton(text="27", callback_data="27")
btn7 = InlineKeyboardButton(text="Назад", callback_data="back")
block_inl = InlineKeyboardMarkup().add(btn8, btn9, btn10, btn11, btn12, btn13, main_m)

#choose stage menu (14-24)

btn14 = InlineKeyboardButton(text="2", callback_data="2")
btn15 = InlineKeyboardButton(text="3", callback_data="3")
btn16 = InlineKeyboardButton(text="4", callback_data="4")
btn17 = InlineKeyboardButton(text="5", callback_data="5")
btn18 = InlineKeyboardButton(text="6", callback_data="6")
btn19 = InlineKeyboardButton(text="7", callback_data="7")
btn20 = InlineKeyboardButton(text="8", callback_data="8")
btn21 = InlineKeyboardButton(text="9", callback_data="9")
btn22 = InlineKeyboardButton(text="10", callback_data="e10")
btn23 = InlineKeyboardButton(text="11", callback_data="e11")
btn24 = InlineKeyboardButton(text="12", callback_data="e12")
stage_inl = InlineKeyboardMarkup().add(btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, main_m)

#choose room

btn25 = InlineKeyboardButton(text="01", callback_data="01")
btn26 = InlineKeyboardButton(text="02", callback_data="02")
btn27 = InlineKeyboardButton(text="03", callback_data="03")
btn28 = InlineKeyboardButton(text="04", callback_data="04")
btn29 = InlineKeyboardButton(text="05", callback_data="05")
btn30 = InlineKeyboardButton(text="06", callback_data="06")
btn31 = InlineKeyboardButton(text="07", callback_data="07")
btn32 = InlineKeyboardButton(text="08", callback_data="08")
btn33 = InlineKeyboardButton(text="09", callback_data="09")
btn34 = InlineKeyboardButton(text="10", callback_data="10")
btn35 = InlineKeyboardButton(text="11", callback_data="11")
btn36 = InlineKeyboardButton(text="12", callback_data="12")
btn37 = InlineKeyboardButton(text="13", callback_data="13")
btn38 = InlineKeyboardButton(text="14", callback_data="14")
btn39 = InlineKeyboardButton(text="15", callback_data="15")
btn40 = InlineKeyboardButton(text="16", callback_data="16")
btn41 = InlineKeyboardButton(text="17", callback_data="17")
btn42 = InlineKeyboardButton(text="18", callback_data="18")
btn43 = InlineKeyboardButton(text="19", callback_data="19")
btn44 = InlineKeyboardButton(text="20", callback_data="20")
btn45 = InlineKeyboardButton(text="21", callback_data="21")
btn46 = InlineKeyboardButton(text="22", callback_data="22")
btn47 = InlineKeyboardButton(text="23", callback_data="23")
btn48 = InlineKeyboardButton(text="24", callback_data="24")
btn49 = InlineKeyboardButton(text="25", callback_data="25")
btn50 = InlineKeyboardButton(text="26", callback_data="26")
btn51 = InlineKeyboardButton(text="27", callback_data="27")
btn52 = InlineKeyboardButton(text="28", callback_data="28")
room_inl = InlineKeyboardMarkup().add(btn25, btn26, btn27, btn28, btn29, btn30, btn31, btn32, btn33, btn34, btn35,
                                   btn36, btn37, btn38, btn39, btn40, btn41, btn42, btn43, btn44, btn45, btn46,
                                   btn47, btn48, btn49, btn50, btn51, btn52, main_m)