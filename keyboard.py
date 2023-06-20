from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_dialog.widgets.kbd import Button, ScrollingGroup

async def start():
	btn1 = InlineKeyboardButton('Наше меню🍕', callback_data='pizza')

	markup = InlineKeyboardMarkup().add(btn1)
	return markup

async def pizza():
	btn1 = InlineKeyboardButton('🍅 Маргарита', callback_data='pizza_1')
	btn2 = InlineKeyboardButton('🌶 Диабло', callback_data='pizza_2')

	btn3 = InlineKeyboardButton('🏳 Народная', callback_data='pizza_3')
	btn4 = InlineKeyboardButton('🇬🇷 Греческая', callback_data='pizza_4')

	btn5 = InlineKeyboardButton('🇮🇹 Итальянская', callback_data='pizza_5')
	btn6 = InlineKeyboardButton('👨‍🎓 Студентическа', callback_data='pizza_6')

	btn7 = InlineKeyboardButton('🥩 Прошутто', callback_data='pizza_7')

	markup = InlineKeyboardMarkup().add(btn1, btn2).add(btn3, btn4).add(btn5, btn6).add(btn7)
	return markup

async def pizza_size():
	btn1 = InlineKeyboardButton('👶 21см Детская', callback_data='kid')
	btn2 = InlineKeyboardButton('📏 26см Маленькая', callback_data='small')

	btn3 = InlineKeyboardButton('🍗 31см Средняя', callback_data='average')
	btn4 = InlineKeyboardButton('👪 36см Семейная', callback_data='family')

	markup = InlineKeyboardMarkup().add(btn1, btn2).add(btn3, btn4)
	return markup

async def repeat():
	btn = InlineKeyboardButton('🔁 Заказать еще', callback_data='repeat_call')
	markup = InlineKeyboardMarkup().add(btn)
	return markup