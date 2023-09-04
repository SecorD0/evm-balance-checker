import asyncio
import logging

from utils.miscellaneous.create_files import create_files
from data import config
from functions.check import check

if __name__ == '__main__':
    try:
        create_files()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(check())

    except BaseException as e:
        logging.exception('main')
        print(f'\n{config.RED}Something went wrong: {e}{config.RESET_ALL}\n')

    input(f'\nPress {config.LIGHTGREEN_EX}Enter{config.RESET_ALL} to exit.\n')
