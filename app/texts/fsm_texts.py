from aiogram.utils.formatting import Bold, as_list, as_marked_section

SUCCESS_FORM = {
    "finish": as_list(
        Bold("Спасибо, данные записаны!\n\n"),
        "Ожидайте, с вами свяжутся в течении трех часов после получения заявки,\
но не ранее чем 8:00 МСК и не позднее чем 18:00 МСК. \
для обсуждения удобного времени для консультации. 👨‍🎓", 
    ).as_html(),   
}