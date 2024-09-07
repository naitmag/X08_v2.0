from app.models import Models
from app.config import LESSONS_PATH
from app.utils import Provider
from datetime import datetime


class LessonsManager:
    """
            A class for lessons management.
    """
    __lessons_path = LESSONS_PATH

    # TODO
    @classmethod
    def read(cls):
        """
            Reads and saves data from raw lessons txt file into the database.
        """
        with open(cls.__lessons_path, 'r', encoding='utf-8') as file:
            text = file.read()
            days = text.split('\n\n\n')

            day_count = 0
            for day in days:

                lessons = day.split('\n\n')
                lesson_number = 0

                for lesson in lessons:

                    items = lesson.split('\n')
                    for item in items:
                        if item != Provider.get_config_value('lessons.empty_lesson_field'):

                            args = item.split(' ')

                            interval = args[0].split('-')

                            if len(interval) < 2:
                                interval.append(interval[0])

                            current_lesson = Lesson(
                                *item.split('"')[1:],
                                lesson_type=args[1],
                                day=day_count,
                                lesson_number=lesson_number,
                                start=interval[0], end=interval[1]
                            )

                            current_lesson.save()

                    lesson_number += 1

                day_count += 1
            return True


class Lesson(Models):
    """
        University lesson model.
    """

    __db_table__ = 'lesson'

    def __init__(self, name: str = None, teacher: str = None,
                 lesson_type: str = None, day: int = None,
                 lesson_number: int = None, start: int | str = None,
                 end: int | str = None, sql_data: tuple = None):
        if sql_data:
            (self.id, self.lesson_type, self.name,
             self.day, self.lesson_number, self.start,
             self.end, self.teacher) = sql_data

            self.name = self.name.capitalize()
            return

        self.name = name
        self.teacher = teacher
        self.lesson_type = lesson_type
        self.day = day
        self.lesson_number = lesson_number
        self.start = start
        self.end = end

    def get_time(self):
        """
        Retrieves lesson time from config.

        :returns: String time
        """

        return Provider.get_config_value(f"lessons.time.{self.lesson_number}")

    def schedule_format(self):
        """
        :returns: String lesson in schedule format.
        """
        return f"- <b>{self.get_time()}</b> {self.lesson_type} <em>{self.name}</em>\n"

    def __str__(self):
        return (f"{self.start}-{self.end} | {self.day} | {self.lesson_number} | "
                f"{self.lesson_type} | {self.name} | {self.teacher}")


class Week:
    """
        Contains lessons info about specific week.
    """

    def __init__(self, number: int = None):
        if number:
            self.number = number
        else:
            self.number = self.get_current_week()

        self.lessons = Lesson.get(start=('<=', self.number), end=('>=', self.number))

    @staticmethod
    def format_weekday(day_number: int, custom_tags: str = None):
        """
            Formats and returns weekday name, uses html tags.

            :arg day_number: weekday number
            :arg custom_tags: comma-separated html tags

            :returns: formatted weekday name
        """

        if custom_tags:
            tags = custom_tags
        else:
            tags = Provider.get_text('schedule.days.tags')

        tags = tags.replace(' ', '')
        tags = tags.split(',')

        emoji = Provider.get_text(f"schedule.days.{day_number}.emoji")
        name = Provider.get_text(f"schedule.days.{day_number}.name")

        prefix = ''
        suffix = ''

        if tags:
            for tag in tags:
                prefix += f"<{tag}>"
                suffix = f"</{tag}>" + suffix

        return f"{emoji} {prefix} {name} {suffix}"

    @staticmethod
    def get_current_week() -> int:
        """
            :returns: current study week.
        """
        start_lessons = Provider.get_config_value('lessons.start')
        date_format = '%d.%m.%Y'
        start_lessons = datetime.strptime(start_lessons, date_format)
        current_date = datetime.now()
        days_difference = (current_date - start_lessons).days

        # shift by 1 day
        # if current day is sunday, user want to see next week schedule
        #                                      vvv
        current_week = round((days_difference + 1) // 7) + 1

        return current_week

    def format_schedule(self):
        """
            :returns: formatted Schedule string
        """
        result = Provider.get_text("schedule.text")
        result += f" {self.number}\n"

        if not self.lessons:
            result += Provider.get_text('schedule.empty_week')
            return result

        day = None
        for lesson in self.lessons:

            lesson = Lesson(sql_data=lesson)
            if day != lesson.day:
                day = lesson.day
                result += "\n" + self.format_weekday(day) + "\n"

            result += lesson.schedule_format()

        return result
