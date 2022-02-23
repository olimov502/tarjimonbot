from aiogram import types

from aiogram.types import ContentType, InputFile
from loader import dp
from loader import bot


# Echo bot
@dp.message_handler(commands='salom')
async def bot_echo(message: types.Message):

    user = message.from_user.id
    video_manzil = InputFile('photos/file_2.jpg')
    await bot.send_photo(chat_id=user, photo=video_manzil)







