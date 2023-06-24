# import os
# import logging
# import datetime
# from functools import wraps
#
#
#
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
#         assert 'Hello World' == hello_world(), "������� ���������� 'Hello World'"
#         result = summator(2, 2)
#         assert isinstance(result, int), '������ ��������� ����� �����'
#         assert result == 4, '2 + 2 = 4'
#         result = div(6, 2)
#         assert result == 3, '6 / 2 = 3'
#         summator(4.3, b=2.2)
#
#     for path in paths:
#
#         assert os.path.exists(path), f'���� {path} ������ ������������'
#
#         with open(path) as log_file:
#             log_file_content = log_file.read()
#
#         assert 'summator' in log_file_content, '������ ���������� ��� �������'
#
#         for item in (4.3, 2.2, 6.5):
#             assert str(item) in log_file_content, f'{item} ������ ���� ������� � ����'
#
#
#
# if __name__ == '__main__':
#     test_2()