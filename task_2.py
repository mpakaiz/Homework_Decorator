# import os
# import logging
# import datetime
# from logging.handlers import RotatingFileHandler
#
#
# def logger_foo(path):
#
#     def __logger(old_function):
#         # logging.basicConfig(filename=f'{path}', encoding='utf-8', level=logging.INFO)
#         __logger = logging.getLogger(path)
#         __logger.setLevel(logging.DEBUG)
#         handler = RotatingFileHandler(path, backupCount=10, maxBytes=1000000)
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         handler.setFormatter(formatter)
#         __logger.addHandler(handler)
#         def new_function(*args, **kwargs):
#             __logger = logging.getLogger(path)
#             print(f'Function {old_function.__name__} executed {datetime.datetime.now()}')
#             __logger.info(f'Function {old_function.__name__} executed {datetime.datetime.now()}')
#             print(f'With args: {args}_{kwargs}')
#             __logger.info(f'With args: {args}_{kwargs}')
#             result = old_function(*args, **kwargs)
#             print(result)
#             __logger.info(f'Result of {old_function.__name__}: {result}')
#             return result
#
#
#         return new_function
#
#     return __logger
#
#
# def test_2():
#     paths = ('log_1.log', 'log_2.log', 'log_3.log')
#
#     for path in paths:
#         if os.path.exists(path):
#             os.remove(path)
#
#         @logger_foo(path)
#         def hello_world():
#             return 'Hello World'
#
#         @logger_foo(path)
#         def summator(a, b=0):
#             return a + b
#
#         @logger_foo(path)
#         def div(a, b):
#             return a / b
#
#         assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
#         result = summator(2, 2)
#         assert isinstance(result, int), 'Должно вернуться целое число'
#         assert result == 4, '2 + 2 = 4'
#         result = div(6, 2)
#         assert result == 3, '6 / 2 = 3'
#         summator(4.3, b=2.2)
#
#     for path in paths:
#
#         assert os.path.exists(path), f'файл {path} должен существовать'
#
#         with open(path) as log_file:
#             log_file_content = log_file.read()
#
#         assert 'summator' in log_file_content, 'должно записаться имя функции'
#
#         for item in (4.3, 2.2, 6.5):
#             assert str(item) in log_file_content, f'{item} должен быть записан в файл'
#
#
#
# if __name__ == '__main__':
#     test_2()