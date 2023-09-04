from typing import Union

from pretty_utils.databases import sqlite

from data.config import ADDRESSES_DB


# --- Functions
def get_address(chain_id: Union[str, int], address: str):
    return db.execute(f"SELECT * FROM '{chain_id}' WHERE address = ?", (address,), fetchone=True, return_class=False)


def get_addresses(chain_id: Union[str, int]):
    return db.execute(f"SELECT * FROM '{chain_id}'", return_class=False)


# --- Miscellaneous
db = sqlite.DB(ADDRESSES_DB)
