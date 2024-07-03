from aiogram import Router, Bot, F
from aiogram import types
from aiogram.types import LabeledPrice
from aiogram.types import ContentType

from app.kb.reply import form_btn


kassa = Router()

@kassa.callback_query(F.data =="success_one")
async def order_consult(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer_invoice(
        title="Онлайн-консультация",
        description="Оплата услуги онлайн-консультирования с экспертом",
        payload="invoice-payload",
        provider_token="381764678:TEST:88233",
        currency="rub",
        prices=[
            LabeledPrice(
                label="Онлайн-консультация",
                amount=100000,
            ),
        ],
        start_parameter="start-parameter",
        photo_url="https://sun9-11.userapi.com/impf/c633927/v633927752/10505/j0YggKmaLB0.jpg?size=398x560&quality=96&sign=69868b97bd365a18c3ee2bb933fee927&type=album",
        photo_size=100,
        photo_height=450,
        photo_width=800,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        request_timeout=15,
    )
    
@kassa.callback_query(F.data =="success_two")
async def order_letter(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer_invoice(
        title="Письмо-претензия",
        description="Оплата услуги подготовки письма-претензии",
        payload="invoice-payload",
        provider_token="381764678:TEST:88233",
        currency="rub",
        prices=[
            LabeledPrice(
                label="Письмо-претензия",
                amount=100000,
            ),
        ],
        start_parameter="start-parameter2",
        photo_url="https://sun9-11.userapi.com/impf/c633927/v633927752/10505/j0YggKmaLB0.jpg?size=398x560&quality=96&sign=69868b97bd365a18c3ee2bb933fee927&type=album",
        photo_size=100,
        photo_height=450,
        photo_width=800,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        request_timeout=15,
    )

@kassa.callback_query(F.data =="success_three")
async def order_isk(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer_invoice(
        title="Исковое заявление",
        description="Оплата услуги подготовки искового заявления",
        payload="invoice-payload",
        provider_token="381764678:TEST:88233",
        currency="rub",
        prices=[
            LabeledPrice(
                label="Исковое заявление",
                amount=100000,
            ),
        ],
        start_parameter="start-parameter3",
        photo_url="https://sun9-11.userapi.com/impf/c633927/v633927752/10505/j0YggKmaLB0.jpg?size=398x560&quality=96&sign=69868b97bd365a18c3ee2bb933fee927&type=album",
        photo_size=100,
        photo_height=450,
        photo_width=800,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        request_timeout=15,
    )
    
    
    

@kassa.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    
    
@kassa.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"Спасибо! Оплата {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошла успешно! 📠\n\n\
Наши менеджеры уже начали обрабатывать заявку, пожалуйста, заполните форму ниже👇", reply_markup=form_btn())