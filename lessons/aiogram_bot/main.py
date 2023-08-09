"""
https://github.com/aiogram/aiogram 4k | 28.8k used
https://github.com/python-telegram-bot/python-telegram-bot 23k | 87.7k
@BotFather
по запросу, человек вводит часть текста (поиск в базе данных)
возможно обмена товаров (создать карточку товара, просмотреть карточки товара, детально об одном товаре, поиск...)
6623784695:AAH39XLQAx5a4EfAlXq0iU4folr59nTKwzE
"""
import datetime
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

# TODO публикация на PythonAnyWhere + Oblako (10 минут - 40 тг| 5000тг) + ps.kz =

bot = Bot(token="6623784695:AAH39XLQAx5a4EfAlXq0iU4folr59nTKwzE")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Register(StatesGroup):
    """Машина состояний - переключатель между функциями"""

    title = State()
    description = State()
    price = State()
    count = State()


@dp.message_handler(state=Register.title)
async def create_title(message: types.Message, state: FSMContext):
    """Ввод наименования товара"""

    await state.update_data(title=str(message.text).strip())
    await message.reply("Введите, <u>описание</u> товара: ❗️", parse_mode="HTML")
    await Register.description.set()


@dp.message_handler(state=Register.description)
async def create_description(message: types.Message, state: FSMContext):
    """Ввод наименования товара"""

    await state.update_data(description=str(message.text).strip())
    await message.reply("Введите, <u>цену</u> товара: ❗️", parse_mode="HTML")
    await Register.price.set()


@dp.message_handler(state=Register.price)
async def create_price(message: types.Message, state: FSMContext):
    """Ввод цены товара"""

    await state.update_data(price=str(message.text).strip())  # todo NO VALIDATE
    await message.reply("Введите, <u>количество</u> товара: ❗️", parse_mode="HTML")
    await Register.count.set()


@dp.message_handler(state=Register.count)
async def create_count(message: types.Message, state: FSMContext):
    """Ввод количества товара"""

    await state.update_data(count=str(message.text).strip())
    item: dict = await state.get_data()

    try:
        Database.create_item(
            item=Item(_id=-1, title=str(item["title"]), description=str(item["description"]), price=float(item["price"]), count=int(item["count"]))
        )

        await message.reply("Товар <b>успешно</b> записан в базу данных!️", parse_mode="HTML")
    except Exception as error:
        await message.reply(f"Товар <b>не  записан</b> в базу данных!️({error})", parse_mode="HTML")
    await state.finish()


class Constants:
    IS_LOG_TO_TXT = True
    IS_LOG_TO_CONSOLE = True


class Models:
    @staticmethod
    def mapping(cls, *args, **kwargs) -> any:
        dict1 = {}
        for k, v in kwargs.items():
            dict1[k] = v

        new_instanse = cls(**dict1)
        return new_instanse


class Item:
    def __init__(self, _id: int, title: str, price: float, description: str, count: int):
        self.id = _id
        self.title = title
        self.price = price
        self.description = description
        self.count = count

    def __str__(self):
        return f"<Item {self.id} {self.title} {self.price} />"

    def has_objects(self):
        """Метод для проверки товара на наличие на складе"""

        # if self.count > 0:
        #     return True
        # else:
        #     return False
        return self.count > 0


class Utils:
    @staticmethod
    def execute_sqlite(query: str, kwargs: dict, many: bool, source: str = "database.db") -> list[tuple] | None:
        try:
            with sqlite3.connect(source) as connection:
                cursor = connection.cursor()
                cursor.execute(query, kwargs)  # todo SQL injection SAFE
                # CRUD
                # i = "id; drop table;"
                # f"select * from sqlite where item = {i}"
                # SELECT it.*, ? trip FROM items it WHERE title = ? and price > ? and title like '%?%'
                # SELECT it.*, :trip trip FROM items it WHERE title = :title and price > :price and title like '%:title%'
                if many:
                    return cursor.fetchall()
                return [cursor.fetchone()]
        except Exception as error:
            err_msg = f"error [{datetime.datetime.now()}] = {error}\n"
            if Constants.IS_LOG_TO_CONSOLE:
                print(err_msg)
            if Constants.IS_LOG_TO_TXT:
                with open("log.txt", mode="a") as file:
                    file.write(err_msg)
            return None


class Database:
    def __init__(self):
        self.create_table_items()

        # Database.create_item(item=Item(_id=-1, title="Проверка", description="Проверка", price=666.6, count=10))

    #         query = """
    # INSERT INTO items
    # (title, description, price, count)
    # VALUES (:title, :description, :price, :count)
    # """
    # for i in range(1, 10):
    #     Utils.execute_sqlite(
    #         query=query,
    #         kwargs={
    #             "title": f"Кроссовки {i}",
    #             "description": f"Кроссовки {i}" * 3,
    #             "price": random.randint(100, 10000),
    #             "count": random.randint(1, 10),
    #         },
    #         many=False,
    #     )

    @staticmethod
    def create_table_items():
        query = """
CREATE TABLE IF NOT EXISTS items
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
description TEXT,
price INTEGER,
count INTEGER
)
"""
        Utils.execute_sqlite(query=query, kwargs={}, many=False)
        print(
            "items: ",
            Utils.execute_sqlite(query="SELECT * from items", kwargs={}, many=True),
        )

    @staticmethod
    def get_items(search: str = "") -> list[Item]:
        # TODO -> API: PHP | PYTHON web
        query = """
SELECT id, title, price, count, description from items
WHERE title LIKE :search
"""
        rows_raw: list[tuple] = Utils.execute_sqlite(query=query, kwargs={"search": f"%{search}%"}, many=True)
        _items: list[Item] = []
        for i in rows_raw:
            _item: Item = Item(
                _id=i[0],
                title=i[1],
                price=i[2],
                count=i[3],
                description=i[4],
            )
            _items.append(_item)

        return _items

    @staticmethod
    def get_item(_id: int) -> Item:
        query = """
SELECT id, title, price, count, description from items
WHERE id = :id
"""
        row_raw: tuple = Utils.execute_sqlite(query=query, kwargs={"id": _id}, many=False)[0]
        _item: Item = Item(
            _id=row_raw[0],
            title=row_raw[1],
            price=row_raw[2],
            count=row_raw[3],
            description=row_raw[4],
        )

        return _item

    @staticmethod
    def create_item(item: Item) -> bool:
        query = """
INSERT INTO items 
(title, price, count, description)
VALUES 
(:title, :price, :count, :description)
"""
        kwargs = {"title": item.title, "price": item.price, "count": item.count, "description": item.description}
        try:
            Utils.execute_sqlite(query=query, kwargs=kwargs, many=False)
            return True
        except Exception as error:
            print(error)
            return False


class Base:
    @staticmethod
    @dp.message_handler(commands=["start", "help"])
    async def f_start(message: types.Message):
        """Запуск бота"""

        await message.reply(
            """
Привет!
Я почти ничего не умею!

Мои возможности:
/items - просмотр всех товаров
/create - публикацию своего товара
"""
        )

    # @staticmethod
    # @dp.message_handler(commands=['start', "help"])
    # async def send_welcome(message: types.Message):
    #     await message.reply("Привет Никита, напиши не что-нибудь!")


class Api:
    pass


class Items:
    @dp.message_handler(commands=["items"])
    async def f_tovars(message: types.Message):
        """Получает список всех товаров из базы данных"""

        # берём из базы данных все товары
        items: list[Item] = Database.get_items()
        # items: list[Item] = []
        # for i in range(1, 10):
        #     item = Item(
        #         _id=i,
        #         title=f"Кроссовки {i}",
        #         price=1000 * i,
        #         description=f"Кроссовки Кроссовки"[:10] + "...",
        #     )
        #     items.append(item)

        # создаю массив кнопок
        _buttons: list[types.InlineKeyboardButton] = []
        for item in items:
            try:
                _button = types.InlineKeyboardButton(
                    text=f"#{item.id} {item.title[:50]} ({item.price} | {item.count})",
                    callback_data=f"get_detail|{item.id}",
                )
                _buttons.append(_button)
            except Exception as error:
                err_msg = f"error [{datetime.datetime.now()}] = {error}\n"
                if Constants.IS_LOG_TO_CONSOLE:
                    print(err_msg)
                if Constants.IS_LOG_TO_TXT:
                    with open("log.txt", mode="a") as file:
                        file.write(err_msg)

        # создание клавиатуры
        _keyboard = types.InlineKeyboardMarkup(row_width=3)
        _keyboard.add(*_buttons)

        await message.reply("Выберите один товар из списка: \n", reply_markup=_keyboard)

    @dp.message_handler(commands=["create"])
    async def f_create(message: types.Message):
        """Выводит кнопку для создания товара"""

        _button = types.InlineKeyboardButton(
            text="Опубликуйте свой товар:",
            callback_data="create_step1",
        )
        _keyboard = types.InlineKeyboardMarkup(row_width=2)
        _keyboard.add(_button)

        await message.reply(
            "Нажмите, чтобы <u>создать карточку</u>:",
            reply_markup=_keyboard,
            parse_mode="HTML",
        )

    @dp.callback_query_handler(lambda callback_query: True)
    async def handle_button_click(callback_query: types.CallbackQuery):
        """Обработка нажатия кнопки"""
        query_data = callback_query.data.split("|")[0]

        if query_data == "get_detail":
            _args = callback_query.data.split("|")[1]
            _pk: int = int(_args)
            # берём из базы данных товар по id
            item: Item = Database.get_item(_id=_pk)
            html = f"""
Наименование: {item.title}
Цена: {item.price}
Описание: {item.description}
Количество на складе: {item.count}

<u>количество</u> товара: ❗️
"""
            await callback_query.message.reply(html, parse_mode="HTML")
        elif query_data == "create_step1":
            await callback_query.message.reply("Введите, <u>название</u> товара: ❗️", parse_mode="HTML")
            await Register.title.set()
        else:
            pass

    # @staticmethod
    # @dp.message_handler()
    # async def echo(message: types.Message):
    #     txt: str = str(message.text)
    #     new_txt = " ".join(txt.split(" ")[::-1])
    #     await message.answer(new_txt)


if __name__ == "__main__":
    print(f"bot started... {datetime.datetime.now()}")
    db = Database()
    executor.start_polling(dp, skip_updates=True)
    print(f"bot stopped... {datetime.datetime.now()}")
