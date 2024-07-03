from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Начать 👨‍🎓', callback_data='start')
        ]
    ]
)


async def survey(num_qu):
    
    qu1 = InlineKeyboardBuilder()
    qu1.add(
        InlineKeyboardButton(text='Да', callback_data=f'{num_qu}_yes'),
        InlineKeyboardButton(text='Нет', callback_data=f'{num_qu}_no')
    )
    return qu1.adjust(2).as_markup()

async def inline_price():
    price = InlineKeyboardBuilder()
    price.add(
        InlineKeyboardButton(text='Узнать стоимость💵', callback_data="price"))
    return price.adjust(1).as_markup()


async def num_surv():
    num = InlineKeyboardBuilder()
    num.add(
        InlineKeyboardButton(text='1', callback_data="num_one"),
        InlineKeyboardButton(text='2', callback_data="num_two"),
        InlineKeyboardButton(text='3', callback_data="num_three"))
    return num.adjust(3).as_markup()


async def success(num):
    success = InlineKeyboardBuilder()
    success.add(
        InlineKeyboardButton(text='Принимаю условия соглашения ✅', callback_data=f"success_{num}"))
    return success.adjust(1).as_markup()

to_main = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="На главную", callback_data="to_main")]]
)