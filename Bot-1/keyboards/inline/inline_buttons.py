from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


inline_fanlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(text='English🇬🇧 - Uzbek🇺🇿', callback_data='n1'),
          InlineKeyboardButton(text='Rus🇷🇺 - Uzbek🇺🇿', callback_data='n2')

        ],
        [
           InlineKeyboardButton(text='Uzbek🇺🇿 - English🇬🇧', callback_data='n3'),
           InlineKeyboardButton(text='Uzbek🇺🇿 - Rus🇷🇺', callback_data='n3')
        ],
        [
            InlineKeyboardButton(text='Ulashish📲', switch_inline_query="🤖Eng yaxshi tarjimon bot!"),
            InlineKeyboardButton(text='Hamkorlik uchun👨🏻‍💻', url='https://t.me/a1mnl')
        ]
    ]
)











