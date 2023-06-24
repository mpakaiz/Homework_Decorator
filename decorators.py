import logging
import datetime


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
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'{datetime.datetime.now()},'
                           f'{old_function.__name__},'
                           f'{args}_{kwargs},'
                           f'{result}'
                           )
            return result

        return new_function

    return __logger
