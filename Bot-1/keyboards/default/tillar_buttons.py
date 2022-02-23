from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

tillarr = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ENG - UZ'),
            KeyboardButton(text='RUS - UZ'),
            KeyboardButton(text='ENG - RUS')
        ],

    ],
    resize_keyboard=True
)