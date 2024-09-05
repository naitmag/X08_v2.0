import os

from environs import Env

env = Env()
env.read_env()

SECRET_TOKEN = env.str('SECRET_TOKEN')

DIRS = {
    'locales': os.path.join('templates', 'locales'),
    'images': os.path.join('templates', 'img'),
}

DATABASE_PATH = os.path.join('database', 'database.db')
LESSONS_PATH = os.path.join('templates', 'lessons', 'lessons.txt')
CONFIG_PATH = os.path.join('config', 'config.yml')

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
