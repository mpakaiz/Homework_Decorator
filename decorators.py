import logging
import datetime
from logging.handlers import RotatingFileHandler


def logger(old_function):

    def new_function(*args, **kwargs):
        logging.basicConfig(filename='main.log', level=logging.INFO)
        print(f'Function {old_function.__name__} executed {datetime.datetime.now()}')
        logging.info(f'Function {old_function.__name__} executed {datetime.datetime.now()}')
        print(f'With args: {args}_{kwargs}')
        logging.info(f'With args: {args}_{kwargs}')
        result = old_function(*args, **kwargs)
        print(result)
        logging.info(f'Result of {old_function.__name__}: {result}')
        return result

    return new_function


def logger_foo(path):

    def __logger(old_function):
        # logging.basicConfig(filename=f'{path}', encoding='utf-8', level=logging.INFO)
        __logger = logging.getLogger(path)
        __logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(path, backupCount=10, maxBytes=1000000)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        __logger.addHandler(handler)

        def new_function(*args, **kwargs):
            __logger = logging.getLogger(path)
            print(f'Function {old_function.__name__} executed {datetime.datetime.now()}')
            __logger.info(f'Function {old_function.__name__} executed {datetime.datetime.now()}')
            print(f'With args: {args}_{kwargs}')
            __logger.info(f'With args: {args}_{kwargs}')
            result = old_function(*args, **kwargs)
            print(result)
            __logger.info(f'Result of {old_function.__name__}: {result}')
            return result

        return new_function

    return __logger
