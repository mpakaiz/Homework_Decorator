import os
import logging
import datetime
from functools import wraps



# def logger(path):
#
#     def __logger(old_function):
#
#
#         def new_function(*args, **kwargs):
#             f = open(f'{path}', "a", encoding='utf-8')
#             logging.basicConfig(filename=f'{path}', encoding='utf-8', level=logging.INFO)
#             print(f'Function {old_function.__name__} executed {datetime.datetime.now()}')
#             logging.info(f'Function {old_function.__name__} executed {datetime.datetime.now()}')
#             print(f'With args: {args}_{kwargs}')
#             logging.info(f'With args: {args}_{kwargs}')
#             result = old_function(*args, **kwargs)
#             print(result)
#             logging.info(f'Result of {old_function.__name__}: {result}')
#             f.close()
#             return result
#
#
#         return new_function
#
#     return __logger



if __name__ == '__main__':
    test_2()