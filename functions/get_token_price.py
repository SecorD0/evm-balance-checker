from typing import Union, List, Dict

from functions.get_random_proxy import get_random_proxy
from utils.miscellaneous.async_get import async_get


async def get_token_price(token_symbols: Union[str, List[str]]) -> Dict[str, float]:
    if isinstance(token_symbols, str):
        token_symbols = [token_symbols]

    token_symbols = [token_symbol.lower() for token_symbol in token_symbols]
    token_dict = {}
    tokens = await async_get(url='https://api.coingecko.com/api/v3/coins/list', proxy=await get_random_proxy())
    for token_symbol in token_symbols:
        for token in tokens:
            if token.get('symbol') == token_symbol:
                token_info = await async_get(
                    f'https://api.coingecko.com/api/v3/coins/{token.get("id")}', proxy=await get_random_proxy()
                )
                if 'market_data' in token_info:
                    token_info = token_info['market_data']
                    if token_info['current_price']:
                        price = token_info['current_price']['usd']
                        token_dict[token_symbol] = price
                        break

    return token_dict
