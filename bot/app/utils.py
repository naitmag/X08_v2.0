from aiogram import types

import yaml
import os
from app import config


class Provider:
    """Receives values from config or locale files"""

    DEFAULT_LOCALE = config.DEFAULT_LOCALE
    DIRS = config.DIRS
    CONFIG = config.CONFIG_PATH

    @classmethod
    def __get_data(cls, path: str, source_file: str, value: str):
        """Protected method for retrieving data from specialized files."""
        if source_file:
            path = os.path.join(path, source_file)

        try:
            with open(path, 'r', encoding='utf-8') as f:
                response = yaml.safe_load(f)
        except Exception as e:
            return f"Error: {str(e)}"

        keys = value.split('.')

        for key in keys:
            if key.isdigit():
                key = int(key)
            response = response.get(key, None)

            if response is None:
                return 'None'

        return response

    @classmethod
    def get_text(cls, value: str, locale: str = DEFAULT_LOCALE):
        """Retrieves and returns localized text strings based on the specified language."""
        source_file = f"{locale}.yml"
        return str(cls.__get_data(cls.DIRS['locales'], source_file, value))

    @classmethod
    def get_image(cls, value: str, locale: str = DEFAULT_LOCALE):
        """Retrieves and returns images in aiogram image format for Telegram messages."""
        file_name = cls.get_text(value, locale)
        image_path = os.path.join(cls.DIRS['images'], file_name)

        return types.FSInputFile(path=image_path)

    @classmethod
    def get_config_value(cls, value: str):
        """Retrieves and returns values from config."""
        return cls.__get_data(cls.CONFIG, '', value)
