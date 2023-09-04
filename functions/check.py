import asyncio

from data import config
from data.models import Settings
from functions.General import General
from functions.all_parsed import all_parsed
from functions.check_balances import check_balances
from functions.get_random_proxy import get_random_proxy
from functions.preparatory_checks import preparatory_checks
from utils.miscellaneous.read_spreadsheet import read_spreadsheet


async def check() -> None:
    error_text = await preparatory_checks()
    if error_text:
        print(f'{config.RED}{error_text}{config.RESET_ALL}')

    else:
        settings = Settings()
        if not await get_random_proxy():
            print(f"{config.LIGHTYELLOW_EX}You didn't specify proxies!{config.RESET_ALL}\n")

        addresses = read_spreadsheet(path=config.ADDRESSES_FILE)
        if addresses:
            await General.import_addresses(settings=settings, addresses=addresses)
            for i in range(5):
                print(f'\n{i + 1} parsing attempt...')
                await check_balances(settings=settings)
                if await all_parsed(settings=settings):
                    break

                if i == 4:
                    print(
                        f'{config.RED}Failed to parse the balances of all tokens and NFTs! '
                        f'Try adding RPC and/or proxies.{config.RESET_ALL}'
                    )

                else:
                    print('Sleeping before the next parsing attempt...')
                    await asyncio.sleep(60)

            await General.export_addresses(settings=settings)

        else:
            print(f"{config.RED}You didn't provide any addresses!{config.RESET_ALL}")
