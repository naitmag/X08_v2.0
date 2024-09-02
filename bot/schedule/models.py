from app.models import Models


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


class Week:

    def __init__(self, number: int):
        self.number = number
        self.lessons = Lesson.get(start=('<=', number), end=('>=', number))
