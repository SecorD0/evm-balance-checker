from dataclasses import dataclass
from typing import Optional, List, Dict

from pretty_utils.miscellaneous.files import read_json
from pretty_utils.type_functions.classes import AutoRepr, Singleton
from py_eth_async.data.models import Network as EVMNetwork

from data import config


# ----- Settings
@dataclass
class General:
    threads: int
    parse_token_price: bool


@dataclass
class NFT:
    contract_address: str
    token_id: Optional[int] = None


@dataclass
class Network:
    name: str
    rpcs: List[EVMNetwork]
    tokens: List[str]
    nfts: Dict[str, NFT]


class Settings(Singleton, AutoRepr):
    def __init__(self) -> None:
        json = read_json(path=config.SETTINGS_FILE)

        # --- General
        general = json['general']
        self.general: General = General(
            threads=general['threads'],
            parse_token_price=general['parse_token_price']
        )

        # --- Networks
        self.networks: List[Network] = []
        for network in json.get('networks', []):
            name = network.get('name')
            if name == 'example':
                continue

            rpcs = []
            for rpc in network.get('rpcs', []):
                rpcs.append(EVMNetwork(name=name, rpc=rpc))

            setting_tokens = network.get('tokens', [])
            if setting_tokens:
                tokens = []
                for token in setting_tokens:
                    if token not in tokens:
                        tokens.append(token)

            else:
                tokens = ['']

            nfts = {}
            for nft in network.get('nfts', []):
                contract_address = nft.get('contract_address')
                if contract_address not in nfts:
                    token_id = nft.get('token_id')
                    if token_id:
                        token_id = int(token_id)

                    nfts[contract_address] = NFT(contract_address=contract_address, token_id=token_id)

            self.networks.append(Network(name=name, rpcs=rpcs, tokens=tokens, nfts=nfts))
