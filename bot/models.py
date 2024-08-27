from aiogram import types

import yaml
import os
import config


class Provider:
    DEFAULT_LOCALE = 'ru'
    DIRS = config.DIRS

    @classmethod
    def __get_data(cls, value: str, locale: str = DEFAULT_LOCALE):
        source_file = f"{locale}.yml"
        path = os.path.join(cls.DIRS['locales'], source_file)

        try:
            with open(path, 'r', encoding='utf-8') as f:
                response = yaml.safe_load(f)
        except Exception as e:
            return f"Error: {str(e)}"

        keys = value.split('.')

        for key in keys:

            response = response.get(key, None)
            if response is None:
                return 'None'

        return response

    @classmethod
    def get_text(cls, value: str, locale: str = DEFAULT_LOCALE):
        return str(cls.__get_data(value, locale))

    @classmethod
    def get_image(cls, value: str, locale: str = DEFAULT_LOCALE):
        file_name = cls.__get_data(value, locale)
        image_path = os.path.join(cls.DIRS['images'], file_name)

        return types.FSInputFile(path=image_path)
