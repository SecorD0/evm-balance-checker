from typing import Optional

import aiohttp


async def async_get(url: str, headers: Optional[dict] = None, **kwargs) -> Optional[dict]:
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url, **kwargs) as response:
            status_code = response.status
            response = await response.json()
            if status_code <= 201:
                return response

            raise Exception(f'Request failed with {status_code} status code!')
