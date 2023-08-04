import sqlite3
import psycopg2


def example1():
    with sqlite3.connect('database/example.db') as _connection:
        _cursor = _connection.cursor()
        name = "o"  # ";drop table postgres;"

        # TODO Create TABLE ###############################################################
        #         _cursor.execute('''
        # CREATE TABLE IF NOT EXISTS users
        # (
        # id INTEGER PRIMARY KEY AUTOINCREMENT,
        # name TEXT NOT NULL,
        # age INTEGER NOT NULL
        # )
        # ''')
        # TODO Create TABLE ###############################################################

        # TODO SQL INJECTION ###############################################################
        SQL_INJECTION: str = f"""
SELECT id, name, age FROM users
WHERE name LIKE '{name}%'
ORDER BY name DESC
"""
        # TODO SQL INJECTION ###############################################################

        # TODO SELECT (READ) ###############################################################
        query: str = """
SELECT id, name, age FROM users
--WHERE name LIKE ?
ORDER BY name DESC
"""
        # _cursor.execute(query, (f'%{name}%',))
        _cursor.execute(query)
        # raw_data: tuple = _cursor.fetchone()
        raw_data: list[tuple] = _cursor.fetchall()
        print("raw_data: ", raw_data)
        # TODO SELECT (READ) ###############################################################

        # TODO INSERT ONE (CREATE) ###############################################################
        #         query: str = """
        # INSERT INTO users
        # (name, age) VALUES
        # (?, ?)
        # """
        #         _cursor.execute(query, ('Bogdan', 25))
        # TODO INSERT ONE (CREATE) ###############################################################

        # TODO INSERT MANY (CREATE) ###############################################################
        #         query: str = """
        # INSERT INTO users
        # (name, age) VALUES
        # (?, ?), (?, ?), (?, ?), (?, ?), (?, ?)
        # """
        #         args = []
        #         for i in range(1, 5+1):
        #             args.append(f"Name {i}")
        #             args.append(i+30)
        #         _cursor.execute(query, args)
        # TODO INSERT MANY (CREATE) ###############################################################

        # TODO DELETE (DELETE) ###############################################################

        #         _cursor.execute("""
        # DELETE FROM users
        # WHERE age < ?
        # """, (35,))

        # TODO DELETE (DELETE) ###############################################################

        # TODO UPDATE (UPDATE) ###############################################################

        _cursor.execute("""
UPDATE users
SET age = age + 1
WHERE age < ?;
""", (50,))

        # TODO UPDATE (UPDATE) ###############################################################
        _connection.commit()  # save
        # _connection.rollback()  # cancel


def example2():
    """
CREATE DATABASE magazine
WITH
OWNER = postgres
ENCODING = 'UTF8'
CONNECTION LIMIT = -1
IS_TEMPLATE = False;
    """

    """
CREATE TABLE public.news
(
id serial NOT NULL,
title character varying(255) UNIQUE,
rating bigint default 0,
PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.news
OWNER to postgres;
    """

    """
SELECT * FROM public.news ORDER BY id ASC 
--INSERT INTO news (title) VALUES ('Потоп'), ('Потоп 2')
    """

    with psycopg2.connect(
        user="postgres",
        password="31284bogdan",
        host="127.0.0.1",
        port="5432",
        dbname="magazine",
    ) as connection:
        with connection.cursor() as cursor:
#             cursor.execute("""
# CREATE TABLE IF NOT EXIST public.news
# (
# id serial NOT NULL,
# title character varying(255) UNIQUE,
# rating bigint default 0,
# PRIMARY KEY (id)
# );
# ALTER TABLE IF EXISTS public.news
# OWNER to postgres;
# """)
            cursor.execute("""INSERT INTO news (title) VALUES (%s), (%s)""", ('Потоп 3', 'Потоп 4'))
            cursor.execute("""SELECT * FROM public.news ORDER BY id ASC """)
            row_raw: list[tuple] = cursor.fetchall()
            print(row_raw)  # [(1, 'Потоп', 0), (2, 'Потоп 2', 0)]
            for idx, i in enumerate(row_raw, 0):
                print(idx, i)

    # процедуры - sql функции (аргументы)
    # последовательности - хранится id последней строки
    # view - наборы
    # триггеры - on_insert, on_delete, on_update
    # partitions - 1 таблица - получает данные интенсивно - 1-3 млн записей, 3 * 30 - 90 млн (15-23Gb)  ! > 50 млн || > 12 Gb
    # Table1
    # Table1_History1
    # Table1_History2

    # Рейд-массив - куча жёстких дисков, собранных в группу для ускорение чтения и надёжность
    # Шардирование - разделение таблицы на подтаблицы, возможно с физическим выносом
    # Кэширование - горячий доступ к данным, возможно с физическим выносом


if __name__ == '__main__':
    example2()
