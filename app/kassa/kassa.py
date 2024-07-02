from aiogram import Router, Bot
from aiogram import types
from aiogram.types import LabeledPrice


async def order_consult(message: types.Message):
    await message.answer_invoice(
        title="Онлайн-консультация",
        description="Оплата услуги онлайн-консультирования с экспертом",
        payload="invoice-payload",
        provider_token="381764678:TEST:88233",
        currency="rub",
        prices=[
            LabeledPrice(
                label="Онлайн-консультация",
                amount=150000,
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
        need_shipping_address=False,
        send_email_to_provider=False,
        send_phone_number_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=False,
        reply_markup=None,
        request_timeout=15,
    )
    


async def pre_checkout_query(pre_checkout: types.PreCheckoutQuery):
    await pre_checkout.answer(ok=True)
    
async def successful_payment(message: types.Message):
    msg = f"Спасибо! Оплата {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошла успешно!"
    await message.answer(msg)