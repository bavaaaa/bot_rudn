from aiogram import executor, types, Bot, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import keyboard, random

bot = Bot(token="5731963629:AAEadLEwhISKPYRQvRfZc0q5MWGQFIpef3I")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Adress_1_1(StatesGroup):
    msg = State()
class Adress_2_1(StatesGroup):
    msg = State()
class Adress_3_1(StatesGroup):
    msg = State()
class Adress_4_1(StatesGroup):
    msg = State()
class Adress_5_1(StatesGroup):
    msg = State()
class Adress_6_1(StatesGroup):
    msg = State()
class Adress_7_1(StatesGroup):
    msg = State()

class Adress_1_2(StatesGroup):
    msg = State()
class Adress_2_2(StatesGroup):
    msg = State()
class Adress_3_2(StatesGroup):
    msg = State()
class Adress_4_2(StatesGroup):
    msg = State()
class Adress_5_2(StatesGroup):
    msg = State()
class Adress_6_2(StatesGroup):
    msg = State()
class Adress_7_2(StatesGroup):
    msg = State()

class Adress_1_3(StatesGroup):
    msg = State()
class Adress_2_3(StatesGroup):
    msg = State()
class Adress_3_3(StatesGroup):
    msg = State()
class Adress_4_3(StatesGroup):
    msg = State()
class Adress_5_3(StatesGroup):
    msg = State()
class Adress_6_3(StatesGroup):
    msg = State()
class Adress_7_3(StatesGroup):
    msg = State()

class Adress_1_4(StatesGroup):
    msg = State()
class Adress_2_4(StatesGroup):
    msg = State()
class Adress_3_4(StatesGroup):
    msg = State()
class Adress_4_4(StatesGroup):
    msg = State()
class Adress_5_4(StatesGroup):
    msg = State()
class Adress_6_4(StatesGroup):
    msg = State()
class Adress_7_4(StatesGroup):
    msg = State()

class Adress_1_1(StatesGroup):
    msg = State()
class Adress_2_1(StatesGroup):
    msg = State()
class Adress_3_1(StatesGroup):
    msg = State()
class Adress_4_1(StatesGroup):
    msg = State()
class Adress_5_1(StatesGroup):
    msg = State()
class Adress_6_1(StatesGroup):
    msg = State()
class Adress_7_1(StatesGroup):
    msg = State()

@dp.message_handler(state=Adress_1_1.msg)
async def send_message(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 120 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()

@dp.message_handler(state=Adress_2_1.msg)
async def send_message(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 120 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_3_1.msg)
async def send_message(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 120 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()

@dp.message_handler(state=Adress_4_1.msg)
async def send_message(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 120 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()

@dp.message_handler(state=Adress_5_1.msg)
async def send_message(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 120 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()

@dp.message_handler(state=Adress_6_1.msg)
async def send_message(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {message.text}
💳 Сумма заказа: 120 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()

@dp.message_handler(state=Adress_7_1.msg)
async def send_message(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 120 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()


@dp.message_handler(state=Adress_1_2.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 200 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_2_2.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 200 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_3_2.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 200 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_4_2.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 200 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_5_2.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 200 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_6_2.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 200 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_7_2.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 200 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()


@dp.message_handler(state=Adress_1_3.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 240 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_2_3.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 240 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_3_3.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 240 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_4_3.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 240 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_5_3.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 240 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_6_3.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 240 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_7_3.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 240 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()


@dp.message_handler(state=Adress_1_4.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 280 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_2_4.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 280 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_3_4.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 280 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_4_4.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 280 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_5_4.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 280 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_6_4.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 280 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()
@dp.message_handler(state=Adress_7_4.msg)
async def send_messag(msg: types.Message, state: FSMContext):
    await msg.answer(f'''
🎉 Ваш заказ успешно оформлен
Номер заказа: #️⃣ {random.randint(1000, 9999)}
Адрес доставки: {msg.text}
💳 Сумма заказа: 280 руб
📲 Скоро с вами свяжется менеджер
🥰 Спасибо за заказ!
''', reply_markup=await keyboard.repeat())
    await state.finish()










@dp.message_handler(commands='start')
async def start_msg(msg:types.Message):
    await msg.answer('Добро пожаловать в нашу пиццерию', reply_markup=await keyboard.start())

@dp.callback_query_handler(text="pizza")
async def pizza_call(call: types.CallbackQuery, state: FSMContext):
    msg = call.message

    await msg.answer('Наше меню', reply_markup=await keyboard.pizza())

@dp.callback_query_handler(text=f'pizza_1')
async def pizza_calls(call: types.CallbackQuery, state: FSMContext):
    msg = call.message

    await msg.delete()
    await msg.answer('Выберете размер', reply_markup=await keyboard.pizza_size())


@dp.callback_query_handler(text=f'pizza_2')
async def pizza_calls(call: types.CallbackQuery, state: FSMContext):
    msg = call.message

    await msg.delete()
    await msg.answer('Выберете размер', reply_markup=await keyboard.pizza_size())

@dp.callback_query_handler(text=f'pizza_3')
async def pizza_calls(call: types.CallbackQuery, state: FSMContext):
    msg = call.message

    await msg.delete()
    await msg.answer('Выберете размер', reply_markup=await keyboard.pizza_size())


@dp.callback_query_handler(text=f'pizza_4')
async def pizza_calls(call: types.CallbackQuery, state: FSMContext):
    msg = call.message

    await msg.delete()
    await msg.answer('Выберете размер', reply_markup=await keyboard.pizza_size())


@dp.callback_query_handler(text=f'pizza_5')
async def pizza_calls(call: types.CallbackQuery, state: FSMContext):
    msg = call.message

    await msg.delete()
    await msg.answer('Выберете размер', reply_markup=await keyboard.pizza_size())


@dp.callback_query_handler(text=f'pizza_6')
async def pizza_calls(call: types.CallbackQuery, state: FSMContext):
    msg = call.message

    await msg.delete()
    await msg.answer('Выберете размер', reply_markup=await keyboard.pizza_size())


@dp.callback_query_handler(text=f'pizza_7')
async def pizza_calls(call: types.CallbackQuery, state: FSMContext):
    msg = call.message

    await msg.delete()
    await msg.answer('Выберете размер', reply_markup=await keyboard.pizza_size())

@dp.callback_query_handler(text = 'kid')
async def kid_size(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('Введите адрес куда доставить пиццу')

    msg = call.message

    if msg.text == 'Выберете размер':
        await Adress_1_1.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_2_1.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_3_1.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_4_1.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_5_1.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_6_1.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_7_1.msg.set()

@dp.callback_query_handler(text = 'small')
async def kid_size(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('Введите адрес куда доставить пиццу')

    msg = call.message

    if msg.text == 'Выберете размер':
        await Adress_1_2.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_2_2.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_3_2.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_4_2.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_5_2.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_6_2.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_7_2.msg.set()

@dp.callback_query_handler(text = 'average')
async def kid_size(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('Введите адрес куда доставить пиццу')

    msg = call.message

    if msg.text == 'Выберете размер':
        await Adress_1_3.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_2_3.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_3_3.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_4_3.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_5_3.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_6_3.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_7_3.msg.set()

@dp.callback_query_handler(text = 'family')
async def kid_size(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('Введите адрес куда доставить пиццу')

    msg = call.message

    if msg.text == 'Выберете размер':
        await Adress_1_4.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_2_4.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_3_4.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_4_4.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_5_4.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_6_4.msg.set()
    if msg.text == 'Выберете размер':
        await Adress_7_4.msg.set()

@dp.callback_query_handler(text = 'repeat_call')
async def repeat_call(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Добро пожаловать в нашу пиццерию', reply_markup=await keyboard.start())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
