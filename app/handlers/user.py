import os
from dotenv import load_dotenv

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import FSInputFile
from aiogram import types
from app.texts.text_for_db import QU1, QU2, START
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums import ContentType


from app.texts.text_for_db import qu1_branch, services_branch
from app.kb.keyboards import num_surv, start_kb, success, survey, inline_price
from config import PATH_TO_CONSULT, PATH_TO_ISK, PATH_TO_LETTER

user = Router()

@user.message(CommandStart())
@user.callback_query(F.data == "to_main")
async def start_cmd(message: types.Message):
    await message.answer(START, reply_markup=start_kb)
    

class Survey(StatesGroup):
    qu1 = State()
    qu2 = State()
    


@user.callback_query(F.data == 'start')
async def start_survey(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(QU1, reply_markup=await survey("qu1"))
    
    
@user.callback_query(F.data.startswith('qu1_'))
async def qu2_survey(callback: types.CallbackQuery):
    answer1 = callback.data.split('_')[1]
    if answer1 == 'no':
        await callback.answer()
        await callback.message.answer(QU2, reply_markup=await survey("qu2"))
    else:
        await callback.answer()
        await callback.message.answer(qu1_branch.get("info"), reply_markup=await inline_price())
        
@user.callback_query(F.data == "price")
async def price_qu1(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(qu1_branch.get("services"), reply_markup= await num_surv())
    

@user.callback_query(F.data.startswith("num_"))
async def serviсes_qu1(callback: types.CallbackQuery):
    load_dotenv()
    id = callback.data.split('_')[1]
    if id == 'one':
        document =  FSInputFile(path=PATH_TO_CONSULT)
        await callback.answer()
        await callback.message.answer_document(document=document, caption=services_branch.get("1"), reply_markup=await success("one"))
    elif id == "two":
        document = FSInputFile(path=PATH_TO_LETTER)
        await callback.answer()
        await callback.message.answer_document(document=document, caption=services_branch.get("2"), reply_markup=await success("two"))
    elif id == "three":
        document = FSInputFile(path=PATH_TO_ISK)
        await callback.answer()
        await callback.message.answer_document(document=document, caption=services_branch.get("3"), reply_markup=await success("three"))



