from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.tillar_buttons import tillarr
from loader import dp,baza
import datetime


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    i = message.from_user.first_name
    username = message.from_user.username
    tg_id = message.from_user.id
    vaqt= datetime.datetime.now()
    try:
       baza.user_qoshish( ismi=i, username=username, tg_id=tg_id, vaqt=vaqt)
    except Exception as d:
        print(d)

    await message.answer(f"Salom, {message.from_user.full_name}! Ingiliz yoki Rus tilidagi so'zni , "
                         f"kiriting.",)



