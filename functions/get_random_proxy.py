import random
from typing import Optional

from pretty_utils.miscellaneous.files import read_lines

from data import config


async def get_random_proxy() -> Optional[str]:
    proxies = read_lines(path=config.PROXIES_FILE, skip_empty_rows=True)
    if proxies:
        proxy = random.choice(proxies)
        if 'http' not in proxy and 'socks5' not in proxy:
            proxy = f'http://{proxy}'

        return proxy
