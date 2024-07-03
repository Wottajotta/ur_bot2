from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def form_btn():
    kb = ReplyKeyboardBuilder()
    kb.add(
        KeyboardButton(text='Заполнить форму 📋'),
        
    ),
    return kb.as_markup(resize_keyboard=True,
        input_field_placeholder='Нажмите на кнопку ниже!.')