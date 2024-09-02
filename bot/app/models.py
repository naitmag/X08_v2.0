import sqlite3

from app import config


class Models:
    __db_table__ = ''

    @staticmethod
    def __execute__(query: str, values=()):

        with sqlite3.connect(config.DATABASE) as con:
            cur = con.cursor()
            data = cur.execute(query, values)

            try:
                return data.fetchall()
            except sqlite3.ProgrammingError as _ex:
                return _ex

    def __create_table__(self, params: str):
        query = f"CREATE TABLE IF NOT EXISTS {self.__db_table__} ({params});"
        return self.__execute__(query)

    def save(self):

        vars = self.__dict__
        keys = list(vars.keys())
        values = list(vars.values())

        columns = ', '.join(keys)

        slots = ', '.join(['?'] * len(keys))

        query = f"INSERT INTO {self.__db_table__} ({columns}) VALUES ({slots});"
        self.__execute__(query, values)

    @classmethod
    def get(cls, **kwargs):
        filters = []
        values = []

        for column, value in kwargs.items():

            if isinstance(value, tuple):
                operator, val = value
            else:
                operator, val = '=', value

            filters.append(f"{column} {operator} ?")
            values.append(val)

        objects_filter = " AND ".join(filters)

        query = f"SELECT * FROM {cls.__db_table__} WHERE {objects_filter};"
        print(query)
        return cls.__execute__(query, values)

    def remove(self):
        ...
