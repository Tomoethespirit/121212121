# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self._age = None
#         self.age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value > 0:
#             self._age = value
#         else:
#             raise ValueError("Возраст должен быть положительным числом")
#
#     def is_adult(self):
#         return self._age >= 18
#
#
#
# try:
#     user1 = User("Alice", 30)
#     print(f"User: {user1.name}, Age: {user1.age}, Is Adult: {user1.is_adult()}")
#     user2 = User("Bob", 15)
#     print(f"User: {user2.name}, Age: {user2.age}, Is Adult: {user2.is_adult()}")
#     user3 = User("Charlie", -5)
# except ValueError as e:
#     print(e)


# class Page:
#     def __init__(self, text: str):
#         self.__text = text
#
#     @property
#     def content(self):
#         return self.__text
#
#     @classmethod
#     def from_book(cls, book, page_num: int):
#         if 0 <= page_num < book.pages:
#             return cls(book.get_page(page_num))
#         else:
#             raise ValueError("Invalid page number")
#
#
# class Book:
#     def __init__(self, content: list[str]):
#         self.__content = content
#         self.pages = len(content)
#
#     def read(self):
#         return "\n".join(self.__content)
#
#     def get_page(self, page_num: int):
#         if 0 <= page_num < self.pages:
#             return self.__content[page_num]
#         else:
#             raise ValueError("Invalid page number")
#
#     @classmethod
#     def from_pages(cls, pages: list[Page]):
#         content = [page.content for page in pages]
#         return cls(content)
#
#
# # Пример работы программы
# page1 = Page("This is the text of page 1.")
# page2 = Page("This is the text of page 2.")
# page3 = Page("This is the text of page 3.")
#
# book = Book.from_pages([page1, page2, page3])
# print(book.read())  # This is the text of page 1.\nThis is the text of page 2.\nThis is the text of page 3.
#
# new_page = Page.from_book(book, 1)
# print(new_page.content)  # This is the text of page 2.


#
# class HistoryList:
#     def __init__(self):
#         self.__data = []
#         self.__addition_history = []
#         self.__deletion_history = []
#
#     def add(self, value):
#         self.__data.append(value)
#         self.__addition_history.append(value)
#
#     def remove(self, index):
#         if 0 <= index < len(self.__data):
#             removed_value = self.__data.pop(index)
#             self.__deletion_history.append(removed_value)
#         else:
#             raise IndexError("Index out of range")
#
#     def get(self, index):
#         if 0 <= index < len(self.__data):
#             return self.__data[index]
#         else:
#             raise IndexError("Index out of range")
#
#     @property
#     def data(self):
#         return tuple(self.__data)
#
#     def addition_history(self):
#         return tuple(self.__addition_history)
#
#     def deletion_history(self):
#         return tuple(self.__deletion_history)
#
#     def get_history(self):
#         return {"add": self.addition_history(), "del": self.deletion_history()}
#
# # Пример работы программы
# history_list = HistoryList()
#
# # Добавление элементов
# history_list.add(10)
# history_list.add(20)
# history_list.add(30)
#
# print(history_list.data)  # (10, 20, 30)
#
# # Удаление элемента
# history_list.remove(1)
#
# print(history_list.data)  # (10, 30)
#
# # Получение истории добавления и удаления
# print(history_list.addition_history())  # (10, 20, 30)
# print(history_list.deletion_history())  # (20)
# print(history_list.get_history())  # {'add': (10, 20, 30), 'del': (20)}



# class Animal:
#     def speek(self):
#         return "No sound"
#
# class Cat(Animal):
#     def speek(self):
#         return "Meow"
#
# class Dog(Animal):
#     def speek(self):
#         return "Woof"
#
# class Parrot(Animal):
#     def speek(self):
#         return "Squawk"
#
# # Пример работы программы
# cat = Cat()
# dog = Dog()
# parrot = Parrot()
# animal = Animal()
#
# print(cat.speek())    # Meow
# print(dog.speek())    # Woof
# print(parrot.speek()) # Squawk
# print(animal.speek()) # No sound
#



# class Color:
#     def __init__(self, r: int, g: int, b: int):
#         self.r = self._validate_color_value(r)
#         self.g = self._validate_color_value(g)
#         self.b = self._validate_color_value(b)
#
#     def _validate_color_value(self, value):
#         return max(0, min(255, value))
#
#     def __add__(self, other):
#         if isinstance(other, Color):
#             return Color(
#                 self._validate_color_value(self.r + other.r),
#                 self._validate_color_value(self.g + other.g),
#                 self._validate_color_value(self.b + other.b)
#             )
#         return NotImplemented
#
#     def __sub__(self, other):
#         if isinstance(other, Color):
#             return Color(
#                 self._validate_color_value(self.r - other.r),
#                 self._validate_color_value(self.g - other.g),
#                 self._validate_color_value(self.b - other.b)
#             )
#         return NotImplemented
#
#     def __str__(self):
#         return f"R: {self.r}, G: {self.g}, B: {self.b}"
#
# # Пример работы программы
# color1 = Color(100, 150, 200)
# color2 = Color(60, 70, 80)
#
# color3 = color1 + color2
# color4 = color1 - color2
#
# print(color3)  # R: 160, G: 220, B: 255
# print(color4)  # R: 40, G: 80, B: 120
#
# # Проверка пределов значений
# color5 = Color(255, 255, 255)
# color6 = Color(10, 20, 30)
# color7 = color5 + color6
#
# print(color7)  # R: 255, G: 255, B: 255
#
# color8 = Color(0, 0, 0)
# color9 = Color(10, 20, 30)
# color10 = color8 - color9
#
# print(color10)  # R: 0, G: 0, B: 0


# class Logger:
#     def log(self, msg: str):
#         raise NotImplementedError("Subclasses should implement this!")
#
# class ConsoleLogger(Logger):
#     def log(self, msg: str):
#         print(msg)
#
# class FileLogger(Logger):
#     def __init__(self, file_path: str):
#         self.file_path = file_path
#
#     def log(self, msg: str):
#         with open(self.file_path, 'a') as file:
#             file.write(msg + '\n')
#
# class SomeDataClass:
#     def __init__(self, logger: Logger):
#         self.__logger = logger
#
#     def some_data_process(self, data: str):
#         print("Starting processing")
#         print(f"Processing {data}")
#         print("Data process finished")
#
#         # Performing logging
#         print("Logging data")
#         self.__logger.log(f"[LOG] Data <{data}> processed!")
#
# # Пример работы программы
#
# # Используем ConsoleLogger
# console_logger = ConsoleLogger()
# data_processor_console = SomeDataClass(console_logger)
# data_processor_console.some_data_process("example_data_console")
#
# # Используем FileLogger
# file_logger = FileLogger("logfile.txt")
# data_processor_file = SomeDataClass(file_logger)
# data_processor_file.some_data_process("example_data_file")
#
