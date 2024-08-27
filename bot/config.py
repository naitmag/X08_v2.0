import os

from environs import Env

env = Env()
env.read_env()

SECRET_TOKEN = env.str('SECRET_TOKEN')

DIRS = {
    'locales': os.path.join('locales'),
    'images': os.path.join('templates', 'img')
}
