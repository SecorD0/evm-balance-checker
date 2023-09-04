import os
import platform
import sys
from pathlib import Path

from colorama import Fore, Style

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()

else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

if platform.system() == 'Windows':
    LIGHTGREEN_EX = ''
    RED = ''
    LIGHTYELLOW_EX = ''
    RESET_ALL = ''

else:
    LIGHTGREEN_EX = Fore.LIGHTGREEN_EX
    RED = Fore.RED
    LIGHTYELLOW_EX = Fore.LIGHTYELLOW_EX
    RESET_ALL = Style.RESET_ALL

FILES_DIR = os.path.join(ROOT_DIR, 'files')

ADDRESSES_DB = os.path.join(FILES_DIR, 'addresses.db')

ERRORS_FILE = os.path.join(FILES_DIR, 'errors.log')

ADDRESSES_FILE = os.path.join(FILES_DIR, 'addresses.xlsx')
PROXIES_FILE = os.path.join(FILES_DIR, 'proxies.txt')
SETTINGS_FILE = os.path.join(FILES_DIR, 'settings.json')
