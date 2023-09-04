import asyncio
import logging
import random

from pretty_utils.type_functions.lists import split_list
from pretty_utils.type_functions.strings import format_number
from py_eth_async.client import Client

from data.models import Settings, Network
from functions.get_network_name import get_network_name
from functions.get_random_proxy import get_random_proxy
from utils.db_api.database import get_addresses, db


async def take_action(sem: asyncio.Semaphore, network: Network, db_address: tuple) -> list:
    async with sem:
        address = db_address[0]
        row = [address]
        for i, token in enumerate(network.tokens):
            try:
                parsed_info = db_address[1 + i]
                if parsed_info is None:
                    client = Client(private_key='', network=random.choice(network.rpcs), proxy=await get_random_proxy())
                    balance = await client.wallet.balance(token=token, address=address)
                    row.append(float(balance.Ether))

                else:
                    row.append(parsed_info)

            except:
                logging.exception(f'token | {token}')
                row.append(None)

        for j, nft in enumerate(network.nfts.values()):
            try:
                parsed_info = db_address[len(network.tokens) + 1 + j]
                if parsed_info is None:
                    client = Client(private_key='', network=random.choice(network.rpcs), proxy=await get_random_proxy())
                    if nft.token_id is not None:
                        contract = await client.contracts.get(
                            contract_address=nft.contract_address,
                            abi=[{
                                'constant': True,
                                'inputs': [{'name': 'owner', 'type': 'address'}, {'name': 'id', 'type': 'uint256'}],
                                'name': 'balanceOf',
                                'outputs': [{'name': '', 'type': 'uint256'}],
                                'payable': False,
                                'stateMutability': 'view',
                                'type': 'function'
                            }]
                        )
                        balance = await contract.functions.balanceOf(address, nft.token_id).call()

                    else:
                        contract = await client.contracts.get(
                            contract_address=nft.contract_address,
                            abi=[{
                                'constant': True,
                                'inputs': [{'name': 'owner', 'type': 'address'}],
                                'name': 'balanceOf',
                                'outputs': [{'name': '', 'type': 'uint256'}],
                                'payable': False,
                                'stateMutability': 'view',
                                'type': 'function'
                            }]
                        )
                        balance = await contract.functions.balanceOf(address).call()

                    row.append(balance)

                else:
                    row.append(parsed_info)

            except:
                logging.exception(f'NFT | {nft}')
                row.append(None)

        return row


async def check_balances(settings: Settings):
    for network in settings.networks:
        print(f'\nChecking {get_network_name(network=network)} network...')
        chain_id = network.rpcs[0].chain_id
        headers = [header[1] for header in db.execute(f"PRAGMA table_info({chain_id})", return_class=False)]
        addresses = get_addresses(chain_id=chain_id)
        address_lists = split_list(s_list=addresses, n=settings.general.threads)
        print('\t'.join(headers))
        for address_list in address_lists:
            sem = asyncio.Semaphore(1000)
            tasks = []
            for db_address in address_list:
                task = asyncio.ensure_future(take_action(sem=sem, network=network, db_address=db_address))
                tasks.append(task)

            responses = asyncio.gather(*tasks)
            for response in await responses:
                values = ''
                for header in headers:
                    if header != 'address':
                        values += f"'{header}' = ?, "

                values = values[:-2]
                db.execute(f"UPDATE '{chain_id}' SET {values} WHERE address = ?", response[1:] + response[:1])
                text = ''
                for value in response:
                    if isinstance(value, (float, int)):
                        text += f'{format_number(value)}\t'

                    else:
                        text += f'{value}\t'

                print(text)
