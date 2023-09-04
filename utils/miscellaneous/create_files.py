from typing import Optional

from pretty_utils.miscellaneous.files import touch, write_json, read_json
from pretty_utils.type_functions.dicts import update_dict

from data import config
from utils.miscellaneous.create_spreadsheet import create_spreadsheet


def create_files() -> None:
    touch(path=config.FILES_DIR)
    create_spreadsheet(path=config.ADDRESSES_FILE, headers=('address',), sheet_name='Addresses')
    touch(path=config.PROXIES_FILE, file=True)

    try:
        current_settings: Optional[dict] = read_json(path=config.SETTINGS_FILE)

    except:
        current_settings = {}

    settings = {
        'general': {
            'threads': 10,
            'parse_token_price': True
        },
        'networks': [
            {
                'name': 'example',
                'rpcs': ['rpc_1', 'rpc_2'],
                'tokens': ['', '0xUSDC', '0xUSDT'],
                'nfts': [
                    {'contract_address': '0x'},
                    {'contract_address': '0x', 'token_id': 0}
                ]
            },
            {
                'name': 'arbitrum',
                'rpcs': [
                    'https://rpc.ankr.com/arbitrum/',
                    'https://endpoints.omniatech.io/v1/arbitrum/one/public'
                ],
                'tokens': [
                    '',  # ETH
                    '0xaf88d065e77c8cC2239327C5EDb3A432268e5831',  # USDC
                    '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9'  # USDT
                ]
            },
            {
                'name': 'optimism',
                'rpcs': [
                    'https://rpc.ankr.com/optimism/',
                    'https://endpoints.omniatech.io/v1/op/mainnet/public'
                ],
                'tokens': [
                    '',  # ETH
                    '0x7f5c764cbc14f9669b88837ca1490cca17c31607',  # USDC
                    '0x94b008aa00579c1307b0ef2c499ad98a8ce58e58'  # USDT
                ],
                'nfts': [
                    {'contract_address': '0xfA14e1157F35E1dAD95dC3F822A9d18c40e360E2'}  # Optimism quest
                ]
            }
        ]
    }
    write_json(path=config.SETTINGS_FILE, obj=update_dict(modifiable=current_settings, template=settings), indent=2)


create_files()
