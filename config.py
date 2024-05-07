HOME_DIR = '/home/student/FinPr'  # путь к папке с проектом

IAM_TOKEN = f'{HOME_DIR}/creds/iam_token.txt'
FOLDER_ID = f'{HOME_DIR}/creds/folder_id.txt'

TOKEN = f'{HOME_DIR}/creds/bot_token.txt'

MAX_USERS = 3
MAX_GPT_TOKENS = 120
COUNT_LAST_MSG = 4

# лимиты для пользователя
MAX_USER_STT_BLOCKS = 10  # 10 аудиоблоков
MAX_USER_TTS_SYMBOLS = 5_000  # 5 000 символов
MAX_USER_GPT_TOKENS = 2_000  # 2 000 токенов
MAX_TTS_SYMBOLS = 200 # ограничение на запрос к tts

LOGS = f'{HOME_DIR}/logs.txt'
DB_FILE = f'{HOME_DIR}/messages.db'
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты веселый собеседник. Общайся с пользователем на "ты" и используй юмор. '
                                            'Поддерживай диалог. Не объясняй пользователю, что ты умеешь и можешь. '
                                            'Изображай человека'}]











