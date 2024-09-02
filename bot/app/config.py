import os

from environs import Env

env = Env()
env.read_env()

SECRET_TOKEN = env.str('SECRET_TOKEN')

DIRS = {
    'locales': os.path.join('locales'),
    'images': os.path.join('templates', 'img'),
}
DATABASE = os.path.join('database', 'database.db')

TABLES = {
    'lesson':
        """
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        name TEXT NOT NULL,
        day INTEGER NOT NULL,
        lesson_number INTEGER NOT NULL,
        start INTEGER NOT NULL,
        end INTEGER NOT NULL,
        teacher TEXT
        """
}
