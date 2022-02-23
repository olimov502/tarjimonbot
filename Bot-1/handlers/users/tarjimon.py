from aiogram import types
from googletrans import Translator
from loader import dp
tarjima = Translator()

# Echo bot

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    matn = message.text
    til = tarjima.detect(message.text).lang

    if til == 'en':
        translt = tarjima.translate(matn, dest='uz', src='en')
        await message.answer(text=f'{translt.text}')

    elif til == 'uz':
        translt = tarjima.translate(matn, dest='en', src='uz')
        await message.answer(text=f'{translt.text}')

    elif til== 'ru':
        translt = tarjima.translate(matn, dest='uz', src='ru')
        await message.answer(text=f'{translt.text}')

