from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.kb.reply import form_btn
from app.texts.fsm_texts import SUCCESS_FORM
from app.kb import keyboards as kb


form = Router()


class Application(StatesGroup):
    name = State(),
    decription = State(),


@form.message(F.text=="Заполнить форму 📋")
async def form_start(message: types.Message, state: FSMContext, session: AsyncSession):
    await message.answer("Введите ваше имя: ", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Application.name)
    
@form.message(F.text)
async def form_name(message: types.Message, state: FSMContext, session: AsyncSession):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Опишите сложившуюся ситуацию: ")
    await state.set_state(Application.decription)
    
  
@form.message(F.text)
async def form_decription(message: types.Message, state: FSMContext, session: AsyncSession):
    decription = message.text
    await state.update_data(decription=decription)
    
    data = await state.get_data()
    try:
        await create_application(session, data)
        await message.answer(SUCCESS_FORM, reply_markup=kb.to_main)
        
    except Exception as e:
        await message.answer(
            f"<strong>Ошибка: {str(e)}</strong>\nЗаполните заявку заново!",
            reply_markup=form_btn(),
        )
        await state.clear()
    await message.answer("Опишите сложившуюся ситуацию: ")
    await state.set_state(Application.decription)  
    
