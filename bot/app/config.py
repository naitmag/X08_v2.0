import os
from environs import Env

# Environment reader
env = Env()
env.read_env()

# Telegram bot token
# Gets from @BotFather
SECRET_TOKEN = env.str('SECRET_TOKEN')

# Sets default messages locale
# Available locales : 'ru'
DEFAULT_LOCALE = 'ru'

# Paths to data
DIRS = {
    'locales': os.path.join('templates', 'locales'),
    'images': os.path.join('templates', 'img'),
}

# Path to SQLite database
DATABASE_PATH = os.path.join('database', 'database.db')
# Path to lessons input in raw format
LESSONS_PATH = os.path.join('templates', 'lessons', 'lessons.txt')
# Path to config
CONFIG_PATH = os.path.join('config', 'config.yml')

# SQLite table configuration
TABLES = {
    'lesson':
        """
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson_type TEXT NOT NULL,
        name TEXT NOT NULL,
        day INTEGER NOT NULL,
        lesson_number INTEGER NOT NULL,
        start INTEGER NOT NULL,
        end INTEGER NOT NULL,
        teacher TEXT
        """
}
