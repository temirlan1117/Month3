from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)


start_button = KeyboardButton('/start')
mem_button = KeyboardButton('/mem')
mem_all_button = KeyboardButton('/mem_all')
music_button = KeyboardButton('/music')
# audio_button = KeyboardButton('/audio')

start.add(start_button, mem_button,
          mem_all_button, music_button )

#========================================================================================
#
start_test = ReplyKeyboardMarkup(resize_keyboard=True,
                                 row_width=2
                                 ).add(KeyboardButton('/start'))