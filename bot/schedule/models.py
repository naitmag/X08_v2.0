from app.models import Models
from app.config import LESSONS_PATH
from app.utils import Provider


class LessonsManager:
    __lessons_path = LESSONS_PATH

    # TODO
    @classmethod
    def read(cls):
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

                            current_lesson = Lesson()
                            current_lesson.name, current_lesson.teacher = item.split('"')[1:]
                            args = item.split(' ')

                            interval = args[0].split('-')

                            if len(interval) < 2:
                                interval.append(interval[0])

                            current_lesson.start, current_lesson.end = interval
                            current_lesson.type, current_lesson.day, current_lesson.lesson_number = args[
                                0], day_count, lesson_number

                            current_lesson.save()

                    lesson_number += 1

                day_count += 1


class Lesson(Models):
    __db_table__ = 'lesson'

    def __init__(self):
        self.name = None
        self.type = None
        self.day = None
        self.lesson_number = None
        self.start = None
        self.end = None
        self.teacher = None

    def __str__(self):
        return f"{self.start}-{self.end} | {self.day} | {self.lesson_number} | {self.type} | {self.name} | {self.teacher}"


class Week:

    def __init__(self, number: int):
        self.number = number
        self.lessons = Lesson.get(start=('<=', number), end=('>=', number))

    # TODO
    def format_schedule(self):
        result = f"Расписание на неделю {self.number}"
        day = 0
        for lesson in self.lessons:
            pass
