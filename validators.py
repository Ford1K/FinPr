import telebot
import logging  # модуль для сбора логов
import math  # математический модуль для округления
# подтягиваем константы из config файла
from config import *
# подтягиваем функции для работы с БД
from database import count_users, count_all_limits
# подтягиваем функцию для подсчета токенов в списке сообщений
from yandex_gpt import *


# настраиваем запись логов в файл
logging.basicConfig(filename=LOGS, level=logging.ERROR, format="%(asctime)s FILE: %(filename)s IN: %(funcName)s MESSAGE: %(message)s", filemode="w")
bot = telebot.TeleBot(TOKEN)
# получаем количество уникальных пользователей, кроме самого пользователя
def check_number_of_users(user_id):
    count = count_users(user_id)
    if count is None:
        return None, "Ошибка при работе с БД"
    if count > MAX_USERS:
        return None, "Превышено максимальное количество пользователей"
    return True, ""

# проверяем, не превысил ли пользователь лимиты на общение с GPT
def is_gpt_token_limit(messages, total_spent_tokens):
    all_tokens = count_gpt_tokens(messages) + total_spent_tokens
    if all_tokens > MAX_USER_GPT_TOKENS:
        return None, f"Превышен общий лимит GPT-токенов {MAX_USER_GPT_TOKENS}"
    return all_tokens, ""


def is_tts_symbol_limit(user_id, text):
    text_symbols = len(text)
    limit_type = 'tts_symbols'

    # Функция из БД для подсчёта всех потраченных пользователем символов
    all_symbols = count_all_limits(user_id, limit_type) + text_symbols

    # Сравниваем all_symbols с количеством доступных пользователю символов
    if all_symbols >= MAX_USER_TTS_SYMBOLS:
        return None, f"Превышен общий лимит SpeechKit TTS {MAX_USER_TTS_SYMBOLS}. Использовано: {all_symbols} символов. Доступно: {MAX_USER_TTS_SYMBOLS - all_symbols}"

    # Сравниваем количество символов в тексте с максимальным количеством символов в тексте
    if text_symbols >= MAX_TTS_SYMBOLS:
        return None, f"Превышен лимит SpeechKit TTS на запрос {MAX_TTS_SYMBOLS}, в сообщении {text_symbols} символов"

    return len(text), None


def is_stt_block_limit(user_id, duration):
    limit_type = 'stt_blocks'

    # Переводим секунды в аудиоблоки
    audio_blocks = math.ceil(duration / 15) # округляем в большую сторону
    # Функция из БД для подсчёта всех потраченных пользователем аудиоблоков
    all_blocks = count_all_limits(user_id, limit_type) + audio_blocks

    # Проверяем, что аудио длится меньше 30 секунд
    if duration >= 30:
        return None, "SpeechKit STT работает с голосовыми сообщениями меньше 30 секунд"

    # Сравниваем all_blocks с количеством доступных пользователю аудиоблоков
    if all_blocks >= MAX_USER_STT_BLOCKS:
        return None, f"Превышен общий лимит SpeechKit STT {MAX_USER_STT_BLOCKS}. Использовано {all_blocks} блоков. Доступно: {MAX_USER_STT_BLOCKS - all_blocks}"

    return audio_blocks, None















